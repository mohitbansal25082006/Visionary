from openai import OpenAI, APIError
from config import OPENAI_API_KEY

def generate_image(prompt, size, quality):
    valid_sizes = ["1024x1024", "1024x1792", "1792x1024"]
    if size not in valid_sizes:
        raise ValueError(f"Invalid size: {size}. Supported sizes: {valid_sizes}")
    valid_qualities = ["standard", "hd"]
    if quality not in valid_qualities:
        raise ValueError(f"Invalid quality: {quality}. Supported qualities: {valid_qualities}")
    print(f"Debug: Prompt = '{prompt}', Size = {size}, Quality = {quality}")  # Debug
    client = OpenAI(api_key=OPENAI_API_KEY)
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            n=1
        )
        image_url = response.data[0].url
        print(f"Debug: Image URL = {image_url}")  # Debug
        return image_url
    except APIError as e:
        raise Exception(f"Image generation failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Image generation failed: {str(e)}")