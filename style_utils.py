def apply_style(caption, style):
    """
    Applies a specific tone/style to the caption based on the selected vibe.
    """
    if style == "trendy":
        return f"{caption} ☀️🌈 #VibesOnly #Aesthetic"
    elif style == "elegant":
        return f"{caption}. A serene reflection of nature's beauty."
    elif style == "funny":
        return f"{caption} 😂 Can't relate! #JustMeThings"
    elif style == "emotional":
        return f"{caption} ❤️ Sometimes, pictures say more than words."
    else:
        return caption


def generate_hashtags_emojis(text):
    """
    Extracts emojis and hashtags based on keyword matches in the text.
    Returns a string of emojis + hashtags.
    """
    keyword_map = {
        "beach": ("🌊", "#BeachVibes"),
        "coffee": ("☕", "#CoffeeTime"),
        "sun": ("☀️", "#SunnyDays"),
        "rain": ("🌧️", "#RainyMood"),
        "girl": ("👧", "#Wanderlust"),
        "cat": ("🐱", "#CatLovers"),
        "child": ("🧒", "#Innocence"),
        "garden": ("🌼", "#NatureLove"),
        "window": ("🪟", "#PeacefulView"),
        "sunset": ("🌇", "#GoldenHour"),
        "sky": ("☁️", "#SkyLovers"),
        "flower": ("🌸", "#FloralVibes"),
        "mountain": ("⛰️", "#MountainViews"),
        "book": ("📖", "#Bookworm"),
        "food": ("🍱", "#Foodie"),
        "city": ("🌆", "#CityLights"),
        "nature": ("🌿", "#NatureLovers")
    }


    hashtags = []
    emojis = []

    for word, (emoji, hashtag) in keyword_map.items():
        if word in text.lower():
            emojis.append(emoji)
            hashtags.append(hashtag)

    return " ".join(emojis + hashtags)


import random

def generate_social_caption(base_caption, platform, tone, length):
    emojis = {
        "instagram": "🧋📸🌈 ",
        "snapchat": "😎🔥💫 ",
        "linkedin": "🧑‍💻🎓🤝🗂️ "
    }

    hashtags = {
        "instagram": "#instagood🧋 #photooftheday🎉 #moment💫 #vibes✨",
        "snapchat": "#snaplife😜 #mood😍 #filteron🔥 #thismoment🤳",
        "linkedin": "#career💼 #success🏆 #networking📈 #workupdate📊"
    }

    phrases = {
        "instagram": ["just vibes", "making memories", "weekend goals"],
        "snapchat": ["feeling myself", "smile mode on", "done for the day"],
        "linkedin": ["Achieving milestones.", "Proud to be part of this journey.", "Professional growth."]
    }

    if tone == "formal" and platform == "linkedin":
        cap = random.choice(phrases["linkedin"])  # Random LinkedIn phrase
    elif tone == "informal":
        cap = random.choice(phrases.get(platform, ["Best moments"]))  # Random informal phrase
    else:
        cap = base_caption  # Fallback to base caption

    styled = f"{cap} {emojis.get(platform, '')} {hashtags.get(platform, '')}"
    return styled


