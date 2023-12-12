import streamlit as st
from PIL import Image, ImageDraw
import face_recognition

def main():
    st.title("Upload image and get all of people's faces back!")

    uploaded_file = st.file_uploader("Choose the image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = face_recognition.load_image_file(uploaded_file)
        face_locations = face_recognition.face_locations(image)

        pil_image = Image.fromarray(image)

        draw = ImageDraw.Draw(pil_image)

        if (face_locations is None or len(face_locations) == 0):
            st.write("No faces found")
            return
    
        for face_location in face_locations:
            top, right, bottom, left = face_location
            draw.rectangle([left, top, right, bottom], outline="green", width=10)

        st.image(pil_image, use_column_width=True)

if __name__ == "__main__":
    main()