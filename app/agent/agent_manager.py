from app.agent.planner import Planner

from app.agent.tool_executor import ToolExecutor

from app.agent.response_aggregator import (
    ResponseAggregator,
)

from app.core.exceptions import PipelineException


class AgentManager:
    """
    Main Agentic AI pipeline.
    """

    def __init__(self):

        self.planner = Planner()

        self.executor = ToolExecutor()

        self.aggregator = ResponseAggregator()

    def run(
        self,
        query: str
    ) -> dict:

        try:

            tools = self.planner.plan(
                query=query
            )

            if not tools:

                return {

                    "status": "success",

                    "answer": (
                        "I'm an Enterprise AI Assistant.\n\n"
                        "I can answer questions related to:\n"
                        "• Enterprise Applications\n"
                        "• Enterprise Documents\n"
                        "• Software Development\n"
                        "• Authentication\n"
                        "• APIs\n"
                        "• Enterprise Databases\n\n"
                        "Please ask a question related to the enterprise knowledge base."
                    ),

                    "total_documents": 0,

                    "citations": []
                }

            tool_outputs = self.executor.execute(

                tools=tools,

                query=query

            )

            # Return directly if only one tool executed
            if len(tool_outputs) == 1:

                return tool_outputs[0]["response"]

            # Aggregate only when multiple tools are used
            answer = self.aggregator.aggregate(

                query=query,

                tool_outputs=tool_outputs

            )

            return {

                "status": "success",

                "answer": answer,

                "tool_outputs": tool_outputs

            }

        except Exception as exception:

            raise PipelineException(
                "Agent execution failed."
            ) from exception