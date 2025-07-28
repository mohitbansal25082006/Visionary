import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "AI Image Generator"
APP_ICON = "🎨"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
IMAGE_SIZES = ["1024x1024", "1024x1792", "1792x1024"]
QUALITY_OPTIONS = ["standard", "hd"]