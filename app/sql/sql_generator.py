from app.core.exceptions import SQLException

from app.llm.llm_manager import LLMManager

from app.sql.base_sql import BaseSQL

from app.sql.prompt_builder import SQLPromptBuilder


class SQLGenerator(BaseSQL):
    """
    Generates SQL using LLM.
    """

    def __init__(self):

        self.llm = LLMManager()

    def generate_sql(
        self,
        query: str,
        schema: str
    ) -> str:

        try:

            prompt = SQLPromptBuilder.build(
                query=query,
                schema=schema
            )

            sql = self.llm.generate(
                prompt
            )

            return sql.strip()

        except Exception as exception:

            raise SQLException(
                "Failed to generate SQL."
            ) from exception