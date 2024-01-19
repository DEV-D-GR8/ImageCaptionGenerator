import streamlit as st
from PIL import Image
from utils import generate_caption

def main():
    st.title("Image Captioning App")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Generate Caption"):
            caption = generate_caption(uploaded_image)
            st.success(f"Generated Caption: {caption}")
            

if __name__ == "__main__":
    main()
