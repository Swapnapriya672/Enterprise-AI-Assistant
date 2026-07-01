from langchain_core.documents import Document

from app.rag.chunking.recursive_chunker import RecursiveChunker


class CodeChunker(RecursiveChunker):
    """
    Chunker for source code documents.
    """

    SUPPORTED_TYPES = {

        "py",
        "java",
        "js",
        "ts",
        "cpp",
        "c",
        "cs",
        "go",
        "php",
        "html",
        "css"
    }

    def chunk(
        self,
        documents: list[Document]
    ) -> list[Document]:

        code_documents = [

            document

            for document in documents

            if document.metadata.get("file_type")
            in self.SUPPORTED_TYPES

        ]

        return super().chunk(code_documents)