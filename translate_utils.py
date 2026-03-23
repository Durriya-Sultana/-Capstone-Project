from transformers import MarianMTModel, MarianTokenizer

def translate_caption(caption, target_lang="hi"):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    translated = model.generate(**tokenizer(caption, return_tensors="pt", padding=True))
    return tokenizer.decode(translated[0], skip_special_tokens=True)
