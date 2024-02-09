import streamlit as st
from PIL import Image, ImageFilter

st.set_page_config(page_title="Editor de Imagenes", page_icon=":snake:")

st.markdown("<h1 style='text-align: center;'>Editor de imagen</h1>", unsafe_allow_html=True)
st.markdown("---")
img = st.file_uploader("Carga tu imagen a editar", type=["jpg", "jpeg", "png", "gif", "tiff", "bmp", "webp"])
size = st.empty()
mode = st.empty()
format_ = st.empty()
info = st.empty()

if img:
    info.markdown("<h2 style='text-align: center;'>Información de la imagen</h2>", unsafe_allow_html=True)
    opened_img = Image.open(img)  # No uses 'with' aquí porque necesitas usar opened_img fuera del bloque if img
    # Ahora puedes acceder a las propiedades de la imagen abierta
    size.markdown(f"<h6>Size: {opened_img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {opened_img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {opened_img.format}</h6>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Redimensionar</h2>", unsafe_allow_html=True)
    width = st.number_input("Ingrese el ancho", value=opened_img.width)
    height = st.number_input("Ingrese el Largo", value=opened_img.height)
    st.markdown("<h2 style='text-align: center;'>Rotación</h2>", unsafe_allow_html=True)
    degree = st.number_input("Ingrese el ángulo de rotación")
    st.markdown("<h2 style='text-align: center;'>Añadir un Filtro</h2>", unsafe_allow_html=True)
    filter = st.selectbox("Escoja el filtro a seleccionar", options=["NINGUNO", "SMOOTH", "EMBOSS", "BLUR"])
    
    btn = st.button("Ajustar")
    if btn:
        edited = opened_img.resize((width, height))
        edited = edited.rotate(degree)
        if filter != "NINGUNO":
            if filter == "SMOOTH":
                edited = edited.filter(ImageFilter.SMOOTH)
            elif filter == "EMBOSS":
                edited = edited.filter(ImageFilter.EMBOSS)
            elif filter == "BLUR":
                edited = edited.filter(ImageFilter.BLUR)
        st.image(edited)
