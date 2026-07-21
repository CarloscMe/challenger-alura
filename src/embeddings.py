# codigo de src/embeddings.py
from langchain_cohere import CohereEmbeddings

from config.settings import COHERE_API_KEY, EMBEDDING_MODEL


def obtener_embeddings():
    """Devuelve el modelo de embeddings de Cohere ya configurado"""
    return CohereEmbeddings(
        cohere_api_key=COHERE_API_KEY,
        model=EMBEDDING_MODEL,
    )