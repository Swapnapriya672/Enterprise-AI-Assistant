import time

from app.core.exceptions import PipelineException

from app.rag.retriever.retriever_manager import RetrieverManager
from app.rag.guardrails.guardrail_manager import GuardrailManager
from app.rag.prompts.prompt_manager import PromptManager

from app.llm.llm_manager import LLMManager

from app.response.response_manager import ResponseManager


class QueryPipeline:
    """
    Complete query pipeline.
    """

    def __init__(self):

        self.retriever = RetrieverManager()

        self.guardrail = GuardrailManager()

        self.prompt_manager = PromptManager()

        self.llm = LLMManager()

        self.response_manager = ResponseManager()

    def run(
        self,
        query: str
    ) -> dict:

        try:

            total_start = time.perf_counter()

            print("=" * 80)
            print("RAG PERFORMANCE TEST")
            print("=" * 80)

            # --------------------------------------------------

            start = time.perf_counter()

            results = self.retriever.retrieve_with_scores(
                query=query
            )

            print(
                f"Retriever : {time.perf_counter() - start:.3f} sec"
            )

            # --------------------------------------------------

            start = time.perf_counter()

            is_valid = self.guardrail.validate(
                results
            )

            print(
                f"Guardrail : {time.perf_counter() - start:.3f} sec"
            )

            if not is_valid:

                print(
                    f"Total : {time.perf_counter() - total_start:.3f} sec"
                )

                return {

                    "status": "success",

                    "answer":
                    (
                        "I'm an Enterprise AI Assistant.\n\n"
                        "Please ask enterprise related questions."
                    ),

                    "total_documents": 0,

                    "citations": []

                }

            # --------------------------------------------------

            documents = [

                document

                for document, score

                in results

            ]

            # --------------------------------------------------

            start = time.perf_counter()

            prompt = self.prompt_manager.process(

                query=query,

                documents=documents

            )

            print(
                f"Prompt Builder : {time.perf_counter() - start:.3f} sec"
            )

            print(
                f"Prompt Length : {len(prompt)} characters"
            )

            # --------------------------------------------------

            start = time.perf_counter()

            answer = self.llm.generate(
                prompt
            )

            print(
                f"LLM : {time.perf_counter() - start:.3f} sec"
            )

            # --------------------------------------------------

            start = time.perf_counter()

            response = self.response_manager.process(

                answer=answer,

                documents=documents

            )

            print(
                f"Response Formatter : {time.perf_counter() - start:.3f} sec"
            )

            # --------------------------------------------------

            print(
                f"Total : {time.perf_counter() - total_start:.3f} sec"
            )

            print("=" * 80)

            return response

        except Exception as exception:

            raise PipelineException(
                "Query pipeline failed."
            ) from exception