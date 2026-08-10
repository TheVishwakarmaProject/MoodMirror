import random

recommendations = {

    "happy": [
        "You're glowing! Put on your favorite song and dance. 💃",
        "Keep that energy going! Do something you've been excited about. ✨",
        "The vibes are good today. Go enjoy the sunshine! ☀️",
        "Call someone you love and share the good mood. 💛",
        "Take a ridiculous amount of photos. You're clearly having a good day. 📸",
        "Do something spontaneous. Future-you can deal with the consequences. 😌",
        "Put on your favorite playlist and let the day happen. 🎧"
    ],

    "sad": [
        "Hey, take a breath. Go for a little walk. 🌿",
        "The world is still pretty. Step outside for a few minutes. 🌎",
        "Put on your comfort music and give yourself some time. 🎵",
        "Be gentle with yourself today. You don't have to fix everything at once. 💙",
        "Make yourself something warm and get comfortable. ☕",
        "You don't have to be productive right now. Just take a moment. 🌙"
        "Take a tiny break and do something that makes you smile. ✨",
    ],

    "angry": [
        "Don't send that message yet. Take a few deep breaths. 😤",
        "Go for a short walk and give yourself some space. 🚶",
        "Pause before reacting. You can deal with this when you're calmer. 🌿",
        "Put your phone down for five minutes. Seriously. 📵",
        "Get some water and give yourself a few quiet minutes. 💧",
        "You can be angry without letting the anger drive the car. Take a pause. 🖤"
        "Take a tiny break and do something that makes you smile. ✨",
    ],

    "fear": [
        "Take a slow breath and look around you. 🌿",
        "Give yourself a moment to breathe and settle down. 💙",
        "Try grounding yourself by noticing five things around you. 🌎",
        "Sit somewhere comfortable and focus on your breathing for a minute. 🫶",
        "You are allowed to pause. You don't have to solve everything immediately. 🌙",
        "Put on something familiar and comforting while you collect yourself. 🎵"
    ],

    "surprise": [
        "Well, something clearly happened. 😂",
        "Take a second to process that plot twist.",
        "Okay, that face says the universe just dropped some new information. 😭",
        "Take a moment. Your brain is still loading. 🧠",
        "Whatever just happened, document the story before you forget it. 📸"
    ],

    "disgust": [
        "Perhaps look literally anywhere else. 😭",
        "Take a little break and reset your mood.",
        "Let's cleanse the vibes. Put on something you actually enjoy. ✨",
        "Look away. Some things simply do not deserve your attention. 😌",
        "Find something pleasant to look at instead. 🌸",
        "Congratulations, your face has filed a formal complaint. 😂"
    ],

    "neutral": [
        "Maybe take a little break and do something fun.",
        "Go get some fresh air and reset for a moment. 🌿",
        "Maybe your brain just needs a snack. 🍫",
        "Nothing dramatic detected. Enjoy the peace while it lasts. 🫠",
        "You look calm. That's suspiciously rare.",
        "You're giving main-character-loading-screen energy. 😌"
    ]
}


def get_recommendation(emotion):
    """Return a random recommendation based on the detected emotion."""

    emotion = emotion.lower()

    if emotion in recommendations:
        return random.choice(recommendations[emotion])

    return "Take a breath and do something kind for yourself. 💛"