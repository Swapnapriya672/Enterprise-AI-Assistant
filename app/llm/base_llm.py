from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Base class for all LLM providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Generate response from LLM.
        """
        pass