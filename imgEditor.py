import streamlit as st
from PIL import Image, ImageFilter
import base64
from io import BytesIO

st.markdown("<h1 style='text-align: center;'>Editor de imagen</h1>", unsafe_allow_html=True)
st.markdown("---")
img_file = st.file_uploader("Carga tu imagen a editar", type=["jpg", "jpeg", "png", "gif", "tiff", "bmp", "webp"])

if img_file is not None:
    img = Image.open(img_file)
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption="Imagen Original")

    width = st.sidebar.number_input("Ingrese el ancho", value=img.width, min_value=1)
    height = st.sidebar.number_input("Ingrese el Largo", value=img.height, min_value=1)
    degree = st.sidebar.slider("Ángulo de rotación", min_value=0, max_value=360, value=0, step=1)
    filter_option = st.sidebar.selectbox("Escoja el filtro a seleccionar", options=["NINGUNO", "SMOOTH", "EMBOSS", "BLUR"])

    btn = st.sidebar.button("Ajustar")
    if btn:
        edited = img.resize((width, height))
        edited = edited.rotate(degree)
        if filter_option != "NINGUNO":
            if filter_option == "SMOOTH":
                edited = edited.filter(ImageFilter.SMOOTH)
            elif filter_option == "EMBOSS":
                edited = edited.filter(ImageFilter.EMBOSS)
            elif filter_option == "BLUR":
                edited = edited.filter(ImageFilter.BLUR)
        with col2:
            st.image(edited, caption="Imagen Editada")
        
        # Función para obtener el enlace de descarga de la imagen
        def get_image_download_link(img, filename="image.png", text="Descargar imagen editada"):
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:image/png;base64,{img_str}" download="{filename}">{text}</a>'
            return href

        # Mostrar el enlace de descarga
        st.sidebar.markdown(get_image_download_link(edited), unsafe_allow_html=True)
else:
    st.write("Por favor, carga una imagen para editar.")
