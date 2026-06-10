class ClarixBaseException(Exception):
    """Base exception for all Clarix application errors."""
    pass

class InvalidFileTypeError(ClarixBaseException):
    """Raised when user uploads unsupported files"""
    pass

class DocumentNotFoundError(ClarixBaseException):
    """Raised when file is not uploaded or file not found """
    pass

class ChunkingError(ClarixBaseException):
    """Raised when Chunking not happended correctly"""
    pass

class EmbeddingError(ClarixBaseException):
    """Raised when Embedding is not working as expected """
    pass

class VectorStoreError(ClarixBaseException):
    """Raised when issue in Vectorsearch and retrivel"""
    pass

class CollectionNotFoundError(ClarixBaseException):
    """Raised when collection is not in the path"""
    pass

class LLMError(ClarixBaseException):
    """Raised when issue on LLM API calling,LLM model server down"""
    pass

class InvalidQueryError(ClarixBaseException):
    """Raised when query is invalid"""
    pass