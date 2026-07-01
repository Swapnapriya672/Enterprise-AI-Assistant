import re

from app.core.exceptions import SQLException


class SQLValidator:
    """
    Validates generated SQL before execution.
    """

    BLOCKED_KEYWORDS = {

        "DROP",

        "DELETE",

        "TRUNCATE",

        "ALTER",

        "UPDATE",

        "INSERT",

        "CREATE",

        "GRANT",

        "REVOKE"

    }

    @staticmethod
    def validate(
        sql: str
    ) -> str:

        try:

            # Remove markdown code blocks

            sql = re.sub(
                r"```sql",
                "",
                sql,
                flags=re.IGNORECASE
            )

            sql = re.sub(
                r"```",
                "",
                sql
            )

            sql = sql.strip()

            # Remove trailing semicolon

            sql = sql.rstrip(";")

            # Validate dangerous SQL

            sql_upper = sql.upper()

            for keyword in SQLValidator.BLOCKED_KEYWORDS:

                if keyword in sql_upper:

                    raise SQLException(
                        f"{keyword} statements are not allowed."
                    )

            # Allow only SELECT statements

            if not sql_upper.startswith("SELECT"):

                raise SQLException(
                    "Only SELECT statements are allowed."
                )

            return sql

        except Exception as exception:

            raise SQLException(
                "SQL validation failed."
            ) from exception