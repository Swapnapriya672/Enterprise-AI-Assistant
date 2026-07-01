from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseRetriever(ABC):
    """
    Base class for document retrievers.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        k: int = 5
    ) -> list[Document]:
        """
        Retrieve relevant documents.
        """
        pass