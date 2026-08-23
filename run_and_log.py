import builtins
import io
import json
import os
import runpy
import sys
import traceback
import types
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Any

from databaselogger import save_execution


def make_json_safe(value: Any) -> Any:
    """
    Convert common Python values into JSON-compatible values.
    """

    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, (list, tuple, set)):
        return [make_json_safe(item) for item in value]

    if isinstance(value, dict):
        return {
            str(key): make_json_safe(item)
            for key, item in value.items()
        }

    return repr(value)


def collect_variables(namespace: dict[str, Any]) -> dict[str, Any]:
    """
    Collect user-created global variables from the executed program.
    Modules, functions, classes, and internal variables are skipped.
    """

    collected = {}

    for name, value in namespace.items():
        if name.startswith("__"):
            continue

        if isinstance(value, types.ModuleType):
            continue

        if callable(value):
            continue

        collected[name] = make_json_safe(value)

    return collected


def run_and_store(file_path: str) -> None:
    target = Path(file_path).expanduser().resolve()

    if not target.exists():
        print(f"File not found: {target}")
        return

    if target.suffix.lower() != ".py":
        print("The selected file must be a Python .py file.")
        return

    try:
        source_code = target.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Cannot read the Python file: {error}")
        return

    captured_stdout = io.StringIO()
    captured_stderr = io.StringIO()
    captured_inputs = []

    original_input = builtins.input
    execution_namespace = {}

    def logged_input(prompt: str = "") -> str:
        """
        Capture every value entered through input().
        """

        value = original_input(prompt)

        captured_inputs.append(
            {
                "prompt": prompt,
                "value": value,
            }
        )

        return value

    builtins.input = logged_input

    execution_status = "SUCCESS"
    error_message = ""

    try:
        with redirect_stdout(captured_stdout), redirect_stderr(captured_stderr):
            execution_namespace = runpy.run_path(
                str(target),
                run_name="__main__",
            )

    except SystemExit as error:
        # A normal sys.exit(0) is considered successful.
        if error.code not in (None, 0):
            execution_status = "FAILED"
            error_message = traceback.format_exc()

    except Exception:
        execution_status = "FAILED"
        error_message = traceback.format_exc()

    finally:
        builtins.input = original_input

    standard_output = captured_stdout.getvalue()
    standard_error = captured_stderr.getvalue()

    if standard_error:
        if error_message:
            error_message += "\n"

        error_message += standard_error

    variables = collect_variables(execution_namespace)

    execution_context = {
        "inputs": captured_inputs,
        "variables": variables,
    }

    variables_json = json.dumps(
        execution_context,
        indent=2,
        ensure_ascii=False,
    )

    # Show the executed program's output in PyCharm.
    if standard_output:
        print(standard_output, end="")

    if error_message:
        print(error_message)

    inserted_id = save_execution(
        file_name=target.name,
        source_code=source_code,
        variables_json=variables_json,
        program_output=standard_output,
        execution_status=execution_status,
        error_message=error_message,
        function_name=None,
    )

    if inserted_id is not None:
        print("\nExecution stored successfully.")
        print("Execution ID:", inserted_id)
        print("Status:", execution_status)


def main() -> None:
    print("Python Execution Logger")
    print("-" * 30)

    file_path = input("Enter the full path of the Python file: ").strip()

    if not file_path:
        print("No file path was entered.")
        return

    run_and_store(file_path)


if __name__ == "__main__":
    main()