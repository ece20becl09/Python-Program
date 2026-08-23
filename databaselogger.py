import os
from typing import Optional

import mysql.connector
from mysql.connector import Error


def save_execution(
    file_name: str,
    source_code: str,
    variables_json: str,
    program_output: str,
    execution_status: str,
    error_message: str = "",
    function_name: Optional[str] = None,
) -> Optional[int]:
    """
    Save one complete Python program execution in MySQL.

    Returns the inserted row ID when successful.
    Returns None when database logging fails.
    """

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD","NewStrongPassword123!"),
            database=os.getenv("MYSQL_DATABASE", "ashim"),
        )

        cursor = connection.cursor()

        sql = """
            INSERT INTO python_execution_logs (
                file_name,
                function_name,
                variable_name,
                variable_value,
                program_output,
                source_code,
                execution_status,
                error_message
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            file_name,
            function_name,
            "execution_context",
            variables_json,
            program_output,
            source_code,
            execution_status,
            error_message,
        )

        cursor.execute(sql, values)
        connection.commit()

        return cursor.lastrowid

    except Error as error:
        print(f"Database logging error: {error}")
        return None

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()