from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseVectorStore(ABC):
    """
    Base class for vector stores.
    """

    @abstractmethod
    def add_documents(
        self,
        documents: list[Document]
    ) -> None:
        """
        Store documents in vector database.
        """
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        k: int = 5
    ) -> list[Document]:
        """
        Search similar documents.
        """
        pass