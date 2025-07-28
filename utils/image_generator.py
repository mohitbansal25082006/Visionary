import openai
from openai import OpenAIError
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_image(prompt, size, quality):
    valid_sizes = ["1024x1024", "1024x1792", "1792x1024"]
    if size not in valid_sizes:
        raise ValueError(f"Invalid size: {size}. Supported sizes: {valid_sizes}")
    
    valid_qualities = ["standard", "hd"]
    if quality not in valid_qualities:
        raise ValueError(f"Invalid quality: {quality}. Supported qualities: {valid_qualities}")
    
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
        )
        image_url = response.data[0].url
        return image_url
    
    except OpenAIError as e:
        raise Exception(f"Image generation failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Image generation failed: {str(e)}")
