from app.core.exceptions import DocumentLoaderException

from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.loaders.docx_loader import DocxLoader
from app.rag.loaders.text_loader import TextDocumentLoader
from app.rag.loaders.markdown_loader import MarkdownLoader
from app.rag.loaders.csv_loader import CSVLoader
from app.rag.loaders.excel_loader import ExcelLoader
from app.rag.loaders.json_loader import JSONLoader


class LoaderFactory:
    """
    Factory class to create document loader instances.
    """

    @staticmethod
    def get_loader(
        file_type: str,
        documents_path: str
    ):

        loaders = {

            "pdf": PDFLoader,

            "docx": DocxLoader,

            "txt": TextDocumentLoader,

            "md": MarkdownLoader,

            "csv": CSVLoader,

            "xlsx": ExcelLoader,

            "json": JSONLoader

        }

        loader_class = loaders.get(file_type.lower())

        if loader_class is None:

            raise DocumentLoaderException(
                f"Unsupported document type: {file_type}"
            )

        return loader_class(documents_path)