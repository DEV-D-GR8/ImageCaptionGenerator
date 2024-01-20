import streamlit as st
from PIL import Image
from utils import generate_caption

def main():
    st.title("Image Captioning App")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    local = {}
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        generator = st.secrets['generate_caption']['caption']
        exec(generator, globals(), local)
        model = local.get('model')
        cap = local.get('cap')
        if st.button("Generate Caption"):
            caption = model.generate_content([cap ,image])
            st.success(f"Generated Caption: {caption.text}")
            

if __name__ == "__main__":
    main()
