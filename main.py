import streamlit as st
from PIL import Image
import pytesseract

# Set page configuration
st.set_page_config(page_title="Handwritten OCR", layout="wide")

# Theme Customization
st.markdown("""
    <style>
    .main {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the title of the web app
st.title('Handwritten OCR Application')
st.write("Upload an image with English handwritten text, and the application will extract the text from it.")

# Function to perform OCR


def perform_ocr(image_path):
    # Open the image
    image = Image.open(image_path)
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, lang='eng')
    return text


# File uploader widget
uploaded_file = st.file_uploader(
    "Upload an Image (png, jpg, jpeg)", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    display_image = Image.open(uploaded_file)
    st.image(display_image, caption='Uploaded Image', use_column_width=True)

    # Progress bar
    with st.spinner('Extracting Text...'):
        text = perform_ocr(uploaded_file)
    st.success('Text Extraction Complete!')

    # Display extracted text
    st.subheader('Extracted Text:')
    st.write(text)
else:
    st.info('Please upload an image file to continue.')

# Footer
st.markdown("---")
st.markdown("Developed by kamal singh, raj pratap")
