from app.core.exceptions import SQLException


class SQLPromptBuilder:
    """
    Builds SQL prompt.
    """

    @staticmethod
    def build(
        query: str,
        schema: str
    ) -> str:

        try:

            return f"""
You are an expert SQL assistant.

Generate a valid MySQL query.

Rules

1. Use only the given schema.

2. Never invent tables.

3. Never invent columns.

4. Return ONLY SQL.

Database Schema

{schema}

User Question

{query}

SQL Query
""".strip()

        except Exception as exception:

            raise SQLException(
                "Failed to build SQL prompt."
            ) from exception