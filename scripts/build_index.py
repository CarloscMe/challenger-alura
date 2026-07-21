# codigo de scripts/build_index.py
# Este script se ejecuta UNA VEZ (o cada vez que cambien los PDFs) para
# generar el indice FAISS. Se corre con: python scripts/build_index.py
import sys
from pathlib import Path

# Permite importar src/ y config/ al ejecutar este script directamente
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.ingest import cargar_documentos, dividir_en_chunks
from src.embeddings import obtener_embeddings
from src.vectorstore_manager import crear_vectorstore, guardar_vectorstore


def main():
    print("Cargando documentos PDF...")
    documentos = cargar_documentos()
    print(f"Se cargaron {len(documentos)} paginas de documentos.")

    print("Dividiendo en chunks...")
    chunks = dividir_en_chunks(documentos)
    print(f"Se generaron {len(chunks)} chunks.")

    print("Generando embeddings con Cohere...")
    embeddings = obtener_embeddings()

    print("Creando indice FAISS...")
    vectorstore = crear_vectorstore(chunks, embeddings)

    print("Guardando indice en disco...")
    guardar_vectorstore(vectorstore)

    print("Indice generado correctamente en vectorstore/faiss_index/")


if __name__ == "__main__":
    main()