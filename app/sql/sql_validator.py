import re

from app.core.exceptions import SQLException


class SQLValidator:
    """
    Cleans, validates and secures generated SQL.
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

            if not sql:

                raise SQLException(
                    "Empty SQL generated."
                )

            # Remove markdown fences

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

            # Keep only the first SQL statement

            match = re.search(

                r"SELECT[\s\S]*?;",

                sql,

                flags=re.IGNORECASE

            )

            if match:

                sql = match.group(0)

            else:

                lines = []

                for line in sql.splitlines():

                    line = line.strip()

                    if not line:

                        continue

                    lines.append(line)

                    if ";" in line:

                        break

                sql = " ".join(lines)

            sql = sql.strip()

            if not sql.endswith(";"):

                sql += ";"

            sql_upper = sql.upper()

            for keyword in SQLValidator.BLOCKED_KEYWORDS:

                if re.search(
                    rf"\b{keyword}\b",
                    sql_upper
                ):

                    raise SQLException(
                        f"{keyword} statements are not allowed."
                    )

            if not sql_upper.startswith("SELECT"):

                raise SQLException(
                    "Only SELECT statements are allowed."
                )

            return sql

        except Exception as exception:

            raise SQLException(
                "SQL validation failed."
            ) from exception