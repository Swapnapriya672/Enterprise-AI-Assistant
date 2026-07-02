from app.core.exceptions import PipelineException


class PlannerPrompt:
    """
    Builds planner prompt.
    """

    @staticmethod
    def build(
        query: str
    ) -> str:

        try:

            return f"""
You are an Enterprise AI Agent.

Your job is to decide which tool(s) should answer the user's query.

You have ONLY two tools.

========================
Tool 1 : SQLTool
========================

Use SQLTool ONLY when the user needs structured data stored in database tables.

Examples:

Show all applications.

List employees.

Find project details.

Show applications using Python.

Count applications.

Average salary.

Never use SQLTool for explanations.


========================
Tool 2 : RAGTool
========================

Use RAGTool ONLY when the user wants explanations, documentation, guides, architecture, policies, APIs or enterprise knowledge.

Examples:

Explain authentication.

Explain JWT.

Authentication architecture.

Leave policy.

API documentation.

Coding standards.

Never use RAGTool for fetching structured database records.


========================
Use BOTH tools ONLY if BOTH are required.

Example:

Show all Python applications and explain their authentication flow.

Return

SQLTool,RAGTool


========================
If the question is unrelated to the enterprise knowledge base

Return

NONE


========================
Return ONLY one of these EXACT values

SQLTool

RAGTool

SQLTool,RAGTool

NONE


User Query

{query}
"""

        except Exception as exception:

            raise PipelineException(
                "Failed to build planner prompt."
            ) from exception