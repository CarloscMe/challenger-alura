# codigo de src/utils.py
def limpiar_texto(texto: str) -> str:
    """Normaliza espacios y saltos de linea sobrantes en un texto"""
    return " ".join(texto.split())


def formatear_fuentes(documentos_fuente):
    """Extrae los nombres de archivo unicos usados como fuente de una respuesta"""
    fuentes = set()
    for doc in documentos_fuente:
        nombre = doc.metadata.get("source", "documento desconocido")
        fuentes.add(nombre.split("/")[-1].split("\\")[-1])
    return sorted(fuentes)