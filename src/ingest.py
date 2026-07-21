# codigo de src/ingest.py
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from config.settings import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP


def cargar_documentos():
    """Carga todos los PDFs de la carpeta data/documents/"""
    loader = PyPDFDirectoryLoader(str(DATA_DIR))
    documentos = loader.load()
    return documentos


def dividir_en_chunks(documentos):
    """Divide los documentos en fragmentos (chunks) para el indice vectorial"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks = splitter.split_documents(documentos)
    return chunks