from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class DocxLoader(BaseLoader):
    """
    Loader for Microsoft Word documents.
    """

    def load(self) -> list[Document]:

        docx_documents = []

        try:

            docx_files = self.documents_path.glob("*.docx")

            for docx_file in docx_files:

                loader = Docx2txtLoader(str(docx_file))

                documents = loader.load()

                metadata = self.create_metadata(
                    file_path=docx_file,
                    document_type="Word Document"
                )

                for document in documents:

                    document.metadata.update(metadata)

                docx_documents.extend(documents)

            return docx_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load Word documents."
            ) from exception