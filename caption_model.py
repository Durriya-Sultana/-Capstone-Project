from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from style_utils import apply_style, generate_hashtags_emojis

# Load BLIP model and processor once globally
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 📖 Extra storytelling logic for "long" captions
def add_storytelling_context(caption):
    return f"{caption} It was a moment to remember, filled with emotions and a story behind every glance."

# 🔮 Final caption generator function
def generate_caption(image, style="basic", length="medium"):
    # Ensure image is PIL and in RGB
    if not isinstance(image, Image.Image):
        image = Image.open(image).convert('RGB')
    else:
        image = image.convert('RGB')

    # Generate base caption using BLIP
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    base_caption = processor.decode(output[0], skip_special_tokens=True)

    # ✂️ Modify length
    if length == "short":
        caption = base_caption.split(".")[0]
    elif length == "long":
        caption = add_storytelling_context(base_caption)
    else:
        caption = base_caption

    # 🎨 Style application
    styled_caption = apply_style(caption.strip(), style)

    # 🎉 Add emojis and hashtags
    full_caption = styled_caption + " " + generate_hashtags_emojis(caption.lower())

    return full_caption
