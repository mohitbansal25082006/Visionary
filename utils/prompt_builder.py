def enhance_prompt(prompt):
    if not prompt:
        return prompt
    # Simple enhancement: add descriptive keywords
    enhanced = f"{prompt}, highly detailed, vibrant colors, cinematic lighting"
    return enhanced