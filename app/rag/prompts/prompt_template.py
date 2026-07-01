from langchain_core.documents import Document

from app.core.exceptions import PromptException

from app.rag.prompts.base_prompt import BasePrompt
from app.rag.prompts.system_prompt import SYSTEM_PROMPT


class PromptTemplateBuilder(BasePrompt):
    """
    Creates prompts for the LLM.
    """

    def build_prompt(
        self,
        query: str,
        documents: list[Document]
    ) -> str:

        try:

            context = "\n\n".join(

                document.page_content

                for document in documents

            )

            prompt = f"""
{SYSTEM_PROMPT}

Context
--------------------

{context}

--------------------

Question

{query}

Answer
"""

            return prompt.strip()

        except Exception as exception:

            raise PromptException(
                "Failed to build prompt."
            ) from exception