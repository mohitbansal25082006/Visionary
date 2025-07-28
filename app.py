import streamlit as st
from components.sidebar import render_sidebar
from utils.image_generator import generate_image
from utils.loader import display_image
from config import APP_TITLE, APP_ICON

# Configure Streamlit page
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)

# Apply custom CSS if available
try:
    with open("main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("main.css file not found. Proceeding without custom styles.")

# App title
st.title(f"{APP_ICON} {APP_TITLE}")

# Render sidebar inputs
prompt, image_size, quality = render_sidebar()

# Button to trigger image generation
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                # Main image generation
                image_url = generate_image(prompt, image_size, quality)
                display_image(image_url)

            except Exception as e:
                # Handle OpenAI-specific errors or others
                if "content_policy_violation" in str(e):
                    st.error("Your prompt violates OpenAI's content policy. Try again with safer content.")
                else:
                    st.error(f"Error generating image: {str(e)}")
    else:
        st.error("Please enter a prompt to generate an image.")
