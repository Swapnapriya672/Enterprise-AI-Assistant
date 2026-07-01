from app.core.exceptions import IntentException

from app.intent.llm_classifier import LLMClassifier

from app.intent.intent_types import IntentType


class IntentManager:
    """
    Main intent classification pipeline.
    """

    def __init__(self):

        self.classifier = LLMClassifier()

    def classify(
        self,
        query: str
    ) -> IntentType:

        try:

            return self.classifier.classify(
                query=query
            )

        except Exception as exception:

            raise IntentException(
                "Failed to classify user intent."
            ) from exception