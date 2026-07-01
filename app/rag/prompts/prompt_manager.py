from langchain_core.documents import Document

from app.core.exceptions import PromptException

from app.rag.prompts.prompt_template import (
    PromptTemplateBuilder,
)


class PromptManager:
    """
    Main prompt generation pipeline.
    """

    def __init__(self):

        self.builder = PromptTemplateBuilder()

    def process(
        self,
        query: str,
        documents: list[Document]
    ) -> str:

        try:

            return self.builder.build_prompt(
                query=query,
                documents=documents
            )

        except Exception as exception:

            raise PromptException(
                "Failed to generate prompt."
            ) from exception