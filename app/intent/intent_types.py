from enum import Enum


class IntentType(str, Enum):
    """
    Supported intent types.
    """

    SQL = "SQL"

    RAG = "RAG"

    GENERAL = "GENERAL"

    UNKNOWN = "UNKNOWN"