from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):
    """
    Loader for PDF documents.
    """

    def load(self) -> list[Document]:

        pdf_documents = []

        try:

            pdf_files = self.documents_path.glob("*.pdf")

            for pdf_file in pdf_files:

                loader = PyPDFLoader(str(pdf_file))

                documents = loader.load()

                metadata = self.create_metadata(
                    file_path=pdf_file,
                    document_type="PDF Document"
                )

                for document in documents:

                    document.metadata.update(metadata)

                pdf_documents.extend(documents)

            return pdf_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load PDF documents."
            ) from exception