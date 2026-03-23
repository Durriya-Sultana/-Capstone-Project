from flask import Flask, render_template, request
from PIL import Image
from caption_model import generate_caption
from style_utils import generate_social_caption
from translate_utils import translate_caption
from gtts import gTTS
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
AUDIO_FOLDER = "static/audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def speak_caption_gtts(caption, lang="en", filename="caption_audio.mp3"):
    filepath = os.path.join(AUDIO_FOLDER, filename)
    try:
        tts = gTTS(text=caption, lang=lang)
        tts.save(filepath)
        return filename
    except Exception as e:
        print(f"gTTS failed: {e}")
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    basic_caption = None
    sm_caption = None
    image_file = None

    if request.method == "POST":
        if 'submit_basic' in request.form:
            file = request.files.get("image")
            if file:
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                image = Image.open(filepath).convert("RGB")

                lang = request.form.get("language", "None")
                enable_voice = "voice" in request.form

                lang_code = {"None": "en", "Hindi": "hi", "Urdu": "ur"}.get(lang, "en")
                caption = generate_caption(image, style="basic", length="medium")  # plain only

                if lang != "None":
                    caption = translate_caption(caption, target_lang=lang_code)

                audio_path = None
                if enable_voice:
                    filename = f"audio_{random.randint(1000,9999)}.mp3"
                    audio_path = speak_caption_gtts(caption, lang=lang_code, filename=filename)

                basic_caption = {"text": caption, "audio": audio_path}
                image_file = file.filename

        elif 'submit_social' in request.form:
            file = request.files.get("image2")
            if file:
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                image = Image.open(filepath).convert("RGB")
                image_file = file.filename
            else:
                existing_image = request.form.get("image_path")
                if existing_image:
                    filepath = os.path.join(UPLOAD_FOLDER,existing_image)
                    image = Image.open(filepath).convert("RGB")
                    image_file = existing_image    

            platform = request.form.get("platform", "instagram").lower()
            tone = request.form.get("tone", "informal").lower()
            length = request.form.get("sm_length", "medium")
            lang = request.form.get("sm_language", "None")
            lang_code = {"None": "en", "Hindi": "hi", "Urdu": "ur"}.get(lang, "en")

            base_caption = generate_caption(image, style="trendy", length=length)
            styled_caption = generate_social_caption(base_caption, platform, tone, length)

            if lang != "None":
                styled_caption = translate_caption(styled_caption, target_lang=lang_code)

            sm_caption = styled_caption

    return render_template("index.html",
                           basic_caption=basic_caption,
                           sm_caption=sm_caption,
                           image=image_file)

if __name__ == "__main__":
    app.run(debug=True)
