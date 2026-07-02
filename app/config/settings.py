from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Paths
DOCUMENTS_PATH = PROJECT_ROOT / "documents"
UPLOADS_PATH = PROJECT_ROOT / "uploads"
VECTOR_STORE_PATH = PROJECT_ROOT / "vector_store"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval
TOP_K = 3

# Models
OLLAMA_MODEL = "qwen2.5:1.5b"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# LLM
TEMPERATURE = 0
MAX_TOKENS = 2048

# API
HOST = "0.0.0.0"
PORT = 8000

# MySQL
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "enterprise_ai"
DB_USERNAME = "root"
DB_PASSWORD = "2014"