from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BasePrompt(ABC):
    """
    Base class for prompt generation.
    """

    @abstractmethod
    def build_prompt(
        self,
        query: str,
        documents: list[Document]
    ) -> str:
        """
        Build the final prompt.
        """
        pass