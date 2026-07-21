# codigo de config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env de la raiz del proyecto
load_dotenv()

# ---- Rutas base del proyecto ----
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "documents"
VECTORSTORE_DIR = BASE_DIR / "vectorstore" / "faiss_index"

# ---- API Key de Cohere (se lee desde el .env) ----
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ---- Parametros del modelo de embeddings ----
EMBEDDING_MODEL = "embed-multilingual-v3.0"

# ---- Parametros del modelo de lenguaje (LLM) ----
LLM_MODEL = "command-r"
TEMPERATURE = 0.2

# ---- Parametros de chunking (division de texto) ----
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ---- Parametros de recuperacion (retriever) ----
TOP_K = 4

# ---- Validacion basica ----
if not COHERE_API_KEY:
    raise ValueError(
        "No se encontro COHERE_API_KEY. Verifica que exista un archivo .env "
        "en la raiz del proyecto con tu clave de Cohere."
    )