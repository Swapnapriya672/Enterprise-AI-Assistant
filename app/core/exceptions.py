class EnterpriseAIAssistantException(Exception):
    """Base exception for the application."""
    pass


class DocumentLoaderException(EnterpriseAIAssistantException):
    """Raised when loading a document fails."""
    pass


class LLMException(EnterpriseAIAssistantException):
    """Raised when the LLM call fails."""
    pass

class PreprocessingException(EnterpriseAIAssistantException):
    """Raised when document preprocessing fails."""
    pass

class ChunkingException(EnterpriseAIAssistantException):
    """Raised when chunking fails."""
    pass

class EmbeddingException(EnterpriseAIAssistantException):
    """
    Raised when embedding generation fails.
    """
    pass

class VectorStoreException(EnterpriseAIAssistantException):
    """
    Raised when vector database operations fail.
    """
    pass

class RetrievalException(Exception):
    """
    Raised when document retrieval fails.
    """

    pass

class PromptException(EnterpriseAIAssistantException):
    """
    Raised when prompt generation fails.
    """
    pass

class ResponseException(EnterpriseAIAssistantException):
    """
    Raised when response generation fails.
    """
    pass

class PipelineException(EnterpriseAIAssistantException):
    """
    Raised when pipeline execution fails.
    """
    pass

class IntentException(EnterpriseAIAssistantException):
    """
    Raised when intent classification fails.
    """
    pass

class SQLException(EnterpriseAIAssistantException):
    """
    Raised when SQL pipeline fails.
    """
    pass