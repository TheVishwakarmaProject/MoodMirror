import random

recommendations = {
    "happy": [
        "You're glowing! Put on your favorite song and dance. 💃",
        "Keep that energy going! Do something you've been excited about. ✨",
        "The vibes are good today. Go enjoy the sunshine! ☀️",
        "Call someone you love and share the good mood. 💛"
    ],

    "sad": [
        "Hey, take a breath. Go for a little walk. 🌿",
        "The world is still pretty. Step outside for a few minutes. 🌎",
        "Put on your comfort music and give yourself some time. 🎵",
        "Be gentle with yourself today. You don't have to fix everything at once. 💙"
    ],

    "angry": [
        "Don't send that message yet. Take a few deep breaths. 😤",
        "Go for a short walk and give yourself some space. 🚶",
        "Pause before reacting. You can deal with this when you're calmer. 🌿",
        "Put your phone down for five minutes. Seriously. 📵"
    ],

    "fear": [
        "Take a slow breath and look around you. 🌿",
        "Give yourself a moment to breathe and settle down. 💙",
        "Try grounding yourself by noticing five things around you. 🌎"
    ],

    "surprise": [
        "Well, something clearly happened. 😂",
        "Take a second to process that plot twist.",
        "Whatever happened, breathe first. Then investigate. 👀"
    ],

    "disgust": [
        "Whatever you just saw, perhaps look literally anywhere else. 😭",
        "Take a little break and reset your mood.",
        "Let's cleanse the vibes. Put on something you actually enjoy. ✨"
    ],

    "neutral": [
        "You look suspiciously neutral. Put on some music. 🎵",
        "Maybe take a little break and do something fun.",
        "Your face is giving absolutely nothing. Respectfully. 😭",
        "Go get some fresh air and reset for a moment. 🌿"
    ]
}


def get_recommendation(emotion):
    """Return a random recommendation based on the detected emotion."""

    emotion = emotion.lower()

    if emotion in recommendations:
        return random.choice(recommendations[emotion])

    return "Take a breath and do something kind for yourself. 💛"