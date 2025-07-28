import streamlit as st
from config import IMAGE_SIZES, QUALITY_OPTIONS
from utils.prompt_builder import enhance_prompt

def render_sidebar():
    with st.sidebar:
        st.header("Image Generation Options")
        prompt = st.text_area("Enter your prompt", placeholder="e.g., A futuristic city at sunset")
        image_size = st.selectbox("Image Size", IMAGE_SIZES)
        quality = st.selectbox("Quality", QUALITY_OPTIONS)
        if st.button("Enhance Prompt"):
            enhanced = enhance_prompt(prompt)
            st.write(f"Enhanced Prompt: {enhanced}")
            prompt = enhanced
    return prompt, image_size, quality