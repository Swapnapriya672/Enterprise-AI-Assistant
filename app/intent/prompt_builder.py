from app.core.exceptions import IntentException


class IntentPromptBuilder:
    """
    Builds prompt for intent classification.
    """

    @staticmethod
    def build(
        query: str
    ) -> str:

        try:

            prompt = f"""
You are an intent classifier.

Your job is to classify the user's query.

Return ONLY ONE WORD.

The valid outputs are:

SQL
RAG
GENERAL

Rules:

1. Return exactly one word.
2. Do not explain your answer.
3. Do not add punctuation.
4. Do not write complete sentences.

User Query:

{query}

Answer:
"""

            return prompt.strip()

        except Exception as exception:

            raise IntentException(
                "Failed to build intent prompt."
            ) from exception