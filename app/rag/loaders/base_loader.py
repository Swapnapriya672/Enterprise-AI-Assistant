from abc import ABC, abstractmethod
from pathlib import Path

from langchain_core.documents import Document


class BaseLoader(ABC):
    """
    Base class for all document loaders.
    """

    def __init__(self, documents_path: str):

        self.documents_path = Path(documents_path)

    @abstractmethod
    def load(self) -> list[Document]:
        """
        Load all supported documents and return a list of
        LangChain Document objects.
        """
        pass

    def create_metadata(
        self,
        file_path: Path,
        document_type: str
    ) -> dict:
        """
        Create standard metadata for every document.
        """

        return {

            "file_name": file_path.name,

            "file_type": file_path.suffix.replace(".", "").lower(),

            "file_extension": file_path.suffix,

            "file_path": str(file_path),

            "document_type": document_type
        }