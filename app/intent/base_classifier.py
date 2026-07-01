from abc import ABC, abstractmethod

from app.intent.intent_types import IntentType


class BaseClassifier(ABC):
    """
    Base class for all intent classifiers.
    """

    @abstractmethod
    def classify(
        self,
        query: str
    ) -> IntentType:
        """
        Classify user query.
        """
        pass