from langchain_core.documents import Document

from app.core.exceptions import ResponseException

from app.response.response_formatter import (
    ResponseFormatter,
)

from app.response.citation_formatter import (
    CitationFormatter,
)


class ResponseManager:
    """
    Main response pipeline.
    """

    def __init__(self):

        self.response_formatter = ResponseFormatter()

    def process(
        self,
        answer: str,
        documents: list[Document]
    ) -> dict:

        try:

            response = self.response_formatter.format(
                answer=answer,
                documents=documents
            )

            response["citations"] = (
                CitationFormatter.format(
                    documents
                )
            )

            return response

        except Exception as exception:

            raise ResponseException(
                "Failed to generate response."
            ) from exception