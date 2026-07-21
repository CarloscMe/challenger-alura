# codigo de src/vectorstore_manager.py
from langchain_community.vectorstores import FAISS

from config.settings import VECTORSTORE_DIR


def crear_vectorstore(chunks, embeddings):
    """Crea un indice FAISS a partir de los chunks y los embeddings"""
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def guardar_vectorstore(vectorstore):
    """Guarda el indice FAISS en disco"""
    VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(VECTORSTORE_DIR))


def cargar_vectorstore(embeddings):
    """Carga un indice FAISS ya existente desde disco"""
    vectorstore = FAISS.load_local(
        str(VECTORSTORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )
    return vectorstore