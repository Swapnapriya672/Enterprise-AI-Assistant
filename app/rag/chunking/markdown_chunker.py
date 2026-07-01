from langchain_core.documents import Document

from app.rag.chunking.recursive_chunker import RecursiveChunker


class MarkdownChunker(RecursiveChunker):
    """
    Chunker for Markdown documents.
    """

    def chunk(
        self,
        documents: list[Document]
    ) -> list[Document]:

        markdown_documents = [

            document

            for document in documents

            if document.metadata.get("file_type") == "md"

        ]

        return super().chunk(markdown_documents)