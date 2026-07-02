from app.core.exceptions import PipelineException

from app.llm.llm_manager import LLMManager


class ResponseAggregator:
    """
    Combines outputs from multiple tools into one final response.
    """

    def __init__(self):

        self.llm = LLMManager()

    def aggregate(
        self,
        query: str,
        tool_outputs: list[dict]
    ) -> str:

        try:

            context = ""

            for output in tool_outputs:

                tool = output["tool"]

                response = output["response"]

                context += f"\n\n{tool}\n"

                context += str(response)

            prompt = f"""
You are an Enterprise AI Assistant.

A user asked:

{query}

The following tools were executed.

{context}

Using ONLY the above information,
generate one complete,
professional,
well-formatted answer.

Do not mention SQLTool or RAGTool.

Answer:
"""

            return self.llm.generate(
                prompt
            )

        except Exception as exception:

            raise PipelineException(
                "Failed to aggregate responses."
            ) from exception