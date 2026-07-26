import os
from typing import Optional

import mysql.connector
from mysql.connector import Error


def save_calculation(
    operation_name: str,
    num1: float,
    expression: str,
    status: str,
    num2: Optional[float] = None,
    choice: Optional[int] = None,
    result: Optional[object] = None,
    error_message: Optional[str] = None,
) -> Optional[int]:
    """Save one calculator operation in MySQL."""

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE", "ashim"),
        )

        cursor = connection.cursor()

        sql = """
            INSERT INTO calculator_history (
                application_name,
                operation_name,
                num1,
                num2,
                choice,
                expression,
                result_value,
                execution_status,
                error_message
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            "Advanced Calculator Pro",
            operation_name,
            num1,
            num2,
            choice,
            expression,
            None if result is None else str(result),
            status,
            error_message,
        )

        cursor.execute(sql, values)
        connection.commit()

        return cursor.lastrowid

    except Error as error:
        print("Database logging error:", error)
        return None

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()