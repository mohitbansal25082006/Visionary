import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def display_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        print(f"Debug: Content-Type = {response.headers.get('Content-Type')}")  # Debug
        if not response.headers.get('Content-Type', '').startswith('image/'):
            raise ValueError("Response is not an image")
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Generated Image", use_column_width=True)
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch image: {str(e)}")
    except Exception as e:
        st.error(f"Failed to display image: {str(e)}")