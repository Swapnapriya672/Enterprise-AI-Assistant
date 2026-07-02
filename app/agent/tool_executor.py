from app.core.exceptions import PipelineException

from app.tools.sql_tool import SQLTool
from app.tools.rag_tool import RAGTool


class ToolExecutor:
    """
    Executes the tools selected by the planner.
    """

    def __init__(self):

        self.tools = {

            "SQLTool": SQLTool(),

            "RAGTool": RAGTool()

        }

    def execute(
        self,
        tools: list[str],
        query: str
    ) -> list[dict]:

        try:

            responses = []

            for tool in tools:

                print("=" * 80)
                print(f"Executing {tool}")
                print("=" * 80)

                response = self.tools[tool].run(
                    query=query
                )

                responses.append(

                    {

                        "tool": tool,

                        "response": response

                    }

                )

            return responses

        except Exception as exception:

            print("=" * 80)
            print("Tool Failed")
            print(type(exception))
            print(repr(exception))
            print("=" * 80)

            raise