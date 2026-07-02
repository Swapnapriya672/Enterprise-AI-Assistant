from app.core.exceptions import SQLException


class SQLPromptBuilder:
    """
    Builds SQL generation prompt.
    """

    @staticmethod
    def build(
        query: str,
        schema: str
    ) -> str:

        try:

            return f"""
You are an expert MySQL SQL Generator for an Enterprise AI Assistant.

Your task is to generate exactly one valid MySQL SELECT query.

Database Schema

{schema}

User Question

{query}

Rules

1. Use ONLY the tables and columns provided in the schema.
2. Never invent table names.
3. Never invent column names.
4. Return ONLY executable SQL.
5. Do NOT explain the SQL.
6. Do NOT include markdown such as ```sql.
7. Do NOT include comments.
8. Do NOT include any extra text before or after the SQL.
9. Generate exactly ONE SQL statement.
10. The SQL statement must end with a semicolon.
11. Only SELECT queries are allowed.
12. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE, GRANT or REVOKE statements.
13. If the requested information cannot be answered using the given schema, return exactly:

SELECT 'Unable to answer using available schema.' AS message;

Output:
""".strip()

        except Exception as exception:

            raise SQLException(
                "Failed to build SQL prompt."
            ) from exception