# codigo de tests/test_rag_chain.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.embeddings import obtener_embeddings
from src.vectorstore_manager import cargar_vectorstore
from src.rag_chain import construir_cadena_rag


def test_respuesta_dentro_de_dominio():
    embeddings = obtener_embeddings()
    vectorstore = cargar_vectorstore(embeddings)
    cadena = construir_cadena_rag(vectorstore)

    resultado = cadena.invoke({"input": "Como puedo rastrear mi pedido?"})
    assert "answer" in resultado
    assert len(resultado["answer"]) > 0


def test_respuesta_fuera_de_dominio():
    embeddings = obtener_embeddings()
    vectorstore = cargar_vectorstore(embeddings)
    cadena = construir_cadena_rag(vectorstore)

    resultado = cadena.invoke({"input": "Cual es la capital de Francia?"})
    assert "no estoy programado" in resultado["answer"].lower()