from langchain_ollama import OllamaLLM

from app.core.exceptions import LLMException
from app.llm.base_llm import BaseLLM
from app.config.settings import OLLAMA_MODEL


class OllamaModel(BaseLLM):
    """
    Ollama LLM implementation.
    """

    def __init__(
        self,
        model_name: str | None = None
    ):

        self.llm = OllamaLLM(
            model=model_name or OLLAMA_MODEL
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        try:

            return self.llm.invoke(prompt)

        except Exception as exception:

            raise LLMException(
                "Failed to generate LLM response."
            ) from exception