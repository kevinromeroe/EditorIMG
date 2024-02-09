import streamlit as st
from PIL import Image, ImageFilter
import cv2
import numpy as np

st.markdown("<h1 style='text-align: center;'>Editor de imagen</h1>", unsafe_allow_html=True)
st.markdown("---")
img_file = st.file_uploader("Carga tu imagen a editar", type=["jpg", "jpeg", "png", "gif", "tiff", "bmp", "webp"])

if img_file:
    img = Image.open(img_file)
    st.image(img, caption='Imagen Original')

    st.markdown("<h2 style='text-align: center;'>Redimensionar Imagen</h2>", unsafe_allow_html=True)
    width = st.number_input("Ingrese el ancho", min_value=1, value=img.width, key="width")
    height = st.number_input("Ingrese el alto", min_value=1, value=img.height, key="height")

    st.markdown("<h2 style='text-align: center;'>Rotación</h2>", unsafe_allow_html=True)
    degree = st.number_input("Ingrese el ángulo de rotación", key="rotation")

    st.markdown("<h2 style='text-align: center;'>Añadir un Filtro</h2>", unsafe_allow_html=True)
    filter = st.selectbox("Escoja el filtro a seleccionar", options=["NINGUNO", "SMOOTH", "EMBOSS", "BLUR"], key="filter")

    if st.button("Ajustar"):
        # Convertir PIL Image a OpenCV Image
        img_cv = np.array(img.convert('RGB'))
        img_cv = img_cv[:, :, ::-1].copy()

        # Redimensionar la imagen usando OpenCV
        resized_img_cv = cv2.resize(img_cv, (width, height), interpolation=cv2.INTER_CUBIC)
        
        # Rotar la imagen usando OpenCV
        center = (width // 2, height // 2)
        matrix = cv2.getRotationMatrix2D(center, degree, 1.0)
        rotated_img_cv = cv2.warpAffine(resized_img_cv, matrix, (width, height))

        # Convertir de nuevo a PIL Image para aplicar filtros
        edited_img_pil = Image.fromarray(rotated_img_cv[:, :, ::-1])

        if filter != "NINGUNO":
            if filter == "SMOOTH":
                edited_img_pil = edited_img_pil.filter(ImageFilter.SMOOTH)
            elif filter == "EMBOSS":
                edited_img_pil = edited_img_pil.filter(ImageFilter.EMBOSS)
            elif filter == "BLUR":
                edited_img_pil = edited_img_pil.filter(ImageFilter.BLUR)

        st.image(edited_img_pil, caption='Imagen Editada')