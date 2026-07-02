from app.core.exceptions import LLMException

from app.llm.ollama_llm import OllamaModel


class LLMManager:
    """
    Singleton LLM pipeline.
    """

    _model = None

    def __init__(self):

        try:

            if LLMManager._model is None:

                print("Loading LLM...")

                LLMManager._model = OllamaModel()

            self.model = LLMManager._model

        except Exception as exception:

            raise LLMException(
                "Failed to initialize LLM."
            ) from exception

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