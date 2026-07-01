from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class TextDocumentLoader(BaseLoader):
    """
    Loader for plain text documents.
    """

    def load(self) -> list[Document]:

        text_documents = []

        try:

            text_files = self.documents_path.glob("*.txt")

            for text_file in text_files:

                loader = TextLoader(
                    str(text_file),
                    encoding="utf-8"
                )

                documents = loader.load()

                metadata = self.create_metadata(
                    file_path=text_file,
                    document_type="Text Document"
                )

                for document in documents:

                    document.metadata.update(metadata)

                text_documents.extend(documents)

            return text_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load text documents."
            ) from exception