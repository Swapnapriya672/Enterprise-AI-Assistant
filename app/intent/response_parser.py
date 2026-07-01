from app.core.exceptions import IntentException
from app.intent.intent_types import IntentType


class IntentResponseParser:
    """
    Parses LLM response.
    """

    @staticmethod
    def parse(
        response: str
    ) -> IntentType:

        try:

            response = response.strip().upper()

            if "SQL" in response:

                return IntentType.SQL

            if "RAG" in response:

                return IntentType.RAG

            if "GENERAL" in response:

                return IntentType.GENERAL

            return IntentType.UNKNOWN

        except Exception as exception:

            raise IntentException(
                "Failed to parse intent."
            ) from exception