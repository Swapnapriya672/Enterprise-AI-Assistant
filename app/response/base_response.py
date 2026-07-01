from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseResponse(ABC):
    """
    Base class for response generation.
    """

    @abstractmethod
    def format(
        self,
        answer: str,
        documents: list[Document]
    ) -> dict:
        """
        Format the final response.
        """
        pass