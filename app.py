# codigo de app.py
import streamlit as st

from src.embeddings import obtener_embeddings
from src.vectorstore_manager import cargar_vectorstore
from src.rag_chain import construir_cadena_rag

st.set_page_config(page_title="Asistente de Logistica", page_icon="📦")

st.title("📦 Asistente virtual de logistica")
st.caption("Responde preguntas basadas en la documentacion oficial de la empresa.")


@st.cache_resource
def cargar_cadena_rag():
    """Carga el vectorstore y arma la cadena RAG una sola vez (cache)"""
    embeddings = obtener_embeddings()
    vectorstore = cargar_vectorstore(embeddings)
    rag_chain = construir_cadena_rag(vectorstore)
    return rag_chain


rag_chain = cargar_cadena_rag()

# ---- Historial de conversacion en la sesion ----
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

pregunta = st.chat_input("Escribe tu pregunta sobre envios, pedidos o reembolsos...")

if pregunta:
    st.session_state.mensajes.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.chat_message("assistant"):
        with st.spinner("Consultando la documentacion..."):
            respuesta = rag_chain.invoke({"input": pregunta})
            texto_respuesta = respuesta["answer"]
            st.markdown(texto_respuesta)

    st.session_state.mensajes.append({"role": "assistant", "content": texto_respuesta})