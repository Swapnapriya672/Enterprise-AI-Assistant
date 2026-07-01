from app.core.exceptions import IntentException

from app.intent.base_classifier import BaseClassifier

from app.intent.intent_types import IntentType

from app.intent.prompt_builder import (
    IntentPromptBuilder,
)

from app.intent.response_parser import (
    IntentResponseParser,
)

from app.llm.llm_manager import LLMManager


class LLMClassifier(BaseClassifier):
    """
    LLM based intent classifier.
    """

    def __init__(self):

        self.llm = LLMManager()

    def classify(
        self,
        query: str
    ) -> IntentType:

        try:

            prompt = IntentPromptBuilder.build(
                query=query
            )

            response = self.llm.generate(
                prompt
            )

            intent = IntentResponseParser.parse(
                response
            )

            return intent

        except Exception as exception:

            raise IntentException(
                "Failed to classify intent."
            ) from exception