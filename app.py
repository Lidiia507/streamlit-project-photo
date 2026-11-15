import streamlit as st

st.title("Будемо завантажувати фото та відео")
st.write("Давай спробуємо!")
uploaded_image = st.file_uploader("Оберіть фото", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Завантажене фото", use_container_width=True)
