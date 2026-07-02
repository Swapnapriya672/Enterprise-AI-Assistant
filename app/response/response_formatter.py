from langchain_core.documents import Document

from app.core.exceptions import ResponseException
from app.response.base_response import BaseResponse


class ResponseFormatter(BaseResponse):
    """
    Formats the LLM response.
    """

    def format(
        self,
        answer: str,
        documents: list[Document]
    ) -> dict:

        try:

            return {
                "status": "success",
                "answer": answer.strip(),
                "total_documents": len(documents),
                "citations": []
            }

        except Exception as exception:

            raise ResponseException(
                "Failed to format response."
            ) from exception