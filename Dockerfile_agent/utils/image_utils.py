def norm_image_name(image_name: str) -> str:
    if not image_name:
        raise ValueError("Image name not found")
    
    image_name = image_name.strip()

    if ":" not in image_name:
        return f"{image_name}:latest"
    
    if image_name.endswith(":"):
        return f"{image_name}latest"
    
    return image_name   # ✅ IMPORTANT FIX