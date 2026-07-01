from langchain_core.documents import Document

from app.core.exceptions import ResponseException


class CitationFormatter:
    """
    Generates citations from retrieved documents.
    """

    @staticmethod
    def format(
        documents: list[Document]
    ) -> list[dict]:

        try:

            citations = []

            for document in documents:

                citations.append(
                    {
                        "file_name": document.metadata.get(
                            "file_name"
                        ),
                        "file_type": document.metadata.get(
                            "file_type"
                        ),
                        "source": document.metadata.get(
                            "source"
                        )
                    }
                )

            return citations

        except Exception as exception:

            raise ResponseException(
                "Failed to generate citations."
            ) from exception