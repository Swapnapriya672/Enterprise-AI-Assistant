from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseVectorStore(ABC):
    """
    Base class for all vector databases.
    """

    @abstractmethod
    def add_documents(
        self,
        documents: list[Document]
    ) -> None:
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        k: int = 5
    ) -> list[Document]:
        pass

    @abstractmethod
    def similarity_search_with_score(
        self,
        query: str,
        k: int = 5
    ) -> list[tuple[Document, float]]:
        pass