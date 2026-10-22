import os
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mis Aplicaciones de IA", page_icon="🤖", layout="wide")

st.title("Mis Aplicaciones de Inteligencia Artificial")

# ---------------------------------------------------------------
# Lista de clases y aplicaciones.
# Para agregar una app nueva, copia un bloque {...} dentro de "apps".
# "imagen" es opcional: pon el nombre del archivo (ej. "mi_app.png")
# en la misma carpeta del proyecto, o déjalo en None.
# ---------------------------------------------------------------
CLASES = [
    {
        "fecha": "20 de agosto",
        "titulo": "Clase 6. Desarrollo de aplicaciones web para interfaces multimodales",
        "apps": [
            {
                "nombre": "Mi primera app",
                "descripcion": "Primera aplicación web construida con Streamlit.",
                "url": "https://miprimeraapp-3zbnl3hyzf5nuejslpyaxj.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "Mi segunda app",
                "descripcion": "Segunda aplicación web con más componentes de interfaz.",
                "url": "https://misegundaapp-oyj7hracz5tumqn8xjvzv2.streamlit.app/",
                "imagen": None,
            },
        ],
    },
    {
        "fecha": "27 de agosto",
        "titulo": "Clase 7. Interfaces de voz a texto",
        "apps": [
            {
                "nombre": "Voz a texto",
                "descripcion": "Aplicación que convierte la voz en texto.",
                "url": "https://cerrdmufkzjtk7akp8kier.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "Traductor",
                "descripcion": "Traductor por voz entre distintos idiomas.",
                "url": "https://traductorr-pmv9hkocmacdasgycsmxtr.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "OCR a audio",
                "descripcion": "Extrae el texto de una imagen y lo convierte en audio.",
                "url": "https://ocr-audio-nwetgmm3c4vjgoxkppazvv.streamlit.app/",
                "imagen": None,
            },
        ],
    },
    {
        "fecha": "3 de septiembre",
        "titulo": "Clase 8. Procesamiento de lenguaje natural",
        "apps": [
            {
                "nombre": "Nube de palabras",
                "descripcion": "Genera una nube de palabras a partir de un texto.",
                "url": "https://wordcloud-elrhhykjwcnirxse5g8uj6.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "Análisis de sentimientos",
                "descripcion": "Identifica si un texto expresa un sentimiento positivo, negativo o neutral.",
                "url": "https://sentimenta-bgo4bcp8xljfl5c7ofkz45.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "Procesamiento de texto",
                "descripcion": "Aplicación de procesamiento de lenguaje natural.",
                "url": "https://n6enzi7qpshnuye4fjwjea.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "TF-IDF en español",
                "descripcion": "Calcula la relevancia de las palabras en documentos en español.",
                "url": "https://tdfesp-9gb836dqji4orzbduzhusc.streamlit.app/",
                "imagen": None,
            },
        ],
    },
    {
        "fecha": "17 de septiembre",
        "titulo": "Clase 9. Aplicaciones con visión artificial",
        "apps": [
            {
                "nombre": "Detección de objetos (YOLOv5)",
                "descripcion": "Detecta y clasifica objetos en imágenes con YOLOv5.",
                "url": "https://yolov55-hx8qnmcfsbn8m3rslsxert.streamlit.app/",
                "imagen": None,
            },
            {
                "nombre": "Visión artificial",
                "descripcion": "Aplicación de análisis de imágenes con visión artificial.",
                "url": "https://its4jfemoz2ua72kzqwcen.streamlit.app/",
                "imagen": None,
            },
        ],
    },
]

# ---------------- Barra lateral ----------------
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.divider()
    st.subheader("Contenido")
    for clase in CLASES:
        st.write(f"**{clase['fecha']}** · {clase['titulo']}")


# ---------------- Tarjeta de cada app ----------------
def tarjeta(app):
    with st.container(border=True):
        imagen = app.get("imagen")
        if imagen and os.path.exists(imagen):
            st.image(Image.open(imagen), width=200)
        st.markdown(f"#### {app['nombre']}")
        st.write(app["descripcion"])
        st.link_button("Abrir aplicación", app["url"])


# ---------------- Secciones por clase ----------------
for clase in CLASES:
    st.header(clase["titulo"])
    st.caption(f"📅 {clase['fecha']}")
    columnas = st.columns(3)
    for i, app in enumerate(clase["apps"]):
        with columnas[i % 3]:
            tarjeta(app)
    st.divider()


