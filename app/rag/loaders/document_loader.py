from pathlib import Path

from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.loader_factory import LoaderFactory


class DocumentLoader:
    """
    Loads all supported documents from the given directory.
    """

    def __init__(self, documents_path: str):

        self.documents_path = Path(documents_path)

    def load(self) -> list[Document]:

        documents = []

        try:

            available_file_types = self._get_available_file_types()

            for file_type in available_file_types:

                loader = LoaderFactory.get_loader(
                    file_type=file_type,
                    documents_path=str(self.documents_path)
                )

                documents.extend(loader.load())

            return documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load documents."
            ) from exception

    def _get_available_file_types(self) -> set[str]:
        """
        Returns all supported file extensions available
        in the documents directory.
        """

        supported_extensions = {
            "pdf",
            "docx",
            "txt",
            "md",
            "csv",
            "xlsx",
            "json"
        }

        available_extensions = set()

        for file in self.documents_path.iterdir():

            if file.is_file():

                extension = file.suffix.lower().replace(".", "")

                if extension in supported_extensions:

                    available_extensions.add(extension)

        return available_extensions