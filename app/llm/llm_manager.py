from app.core.exceptions import LLMException

from app.llm.ollama_llm import OllamaModel


class LLMManager:
    """
    Main LLM pipeline.
    """

    def __init__(self):

        self.model = OllamaModel()

    def generate(
        self,
        prompt: str
    ) -> str:

        try:

            return self.model.generate(
                prompt
            )

        except Exception as exception:

            raise LLMException(
                "Failed to generate response."
            ) from exception