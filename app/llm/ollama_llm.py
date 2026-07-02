from langchain_ollama import OllamaLLM

from app.core.exceptions import LLMException
from app.llm.base_llm import BaseLLM
from app.config.settings import OLLAMA_MODEL


class OllamaModel(BaseLLM):
    """
    Singleton Ollama LLM implementation.
    """

    _llm = None

    def __init__(
        self,
        model_name: str | None = None
    ):

        try:

            if OllamaModel._llm is None:

                print("Loading Ollama Model...")

                OllamaModel._llm = OllamaLLM(

                    model=model_name or OLLAMA_MODEL,

                    temperature=0,

                    num_predict=128,
                    
                    keep_alive="30m"

                )

            self.llm = OllamaModel._llm

        except Exception as exception:

            raise LLMException(
                "Failed to initialize Ollama model."
            ) from exception

    def generate(
        self,
        prompt: str
    ) -> str:

        try:

            return self.llm.invoke(
                prompt
            )

        except Exception as exception:

            raise LLMException(
                "Failed to generate LLM response."
            ) from exception