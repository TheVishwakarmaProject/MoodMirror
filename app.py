import streamlit as st
import numpy as np
from deepface import DeepFace
from recommendations import get_recommendation


# -----------------------------------
# PAGE SETTINGS
# -----------------------------------

st.set_page_config(
    page_title="MoodMirror",
    page_icon="😊",
    layout="centered"
)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.main {
    background-color: #0f0f14;
}

h1 {
    text-align: center;
    color: #ffffff;
    font-size: 3rem;
}

.subtitle {
    text-align: center;
    color: #b8b8c5;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

.result-box {
    background-color: #1d1d27;
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
}

.emotion {
    font-size: 2rem;
    font-weight: bold;
    color: #66ffb3;
}

.recommendation {
    font-size: 1.2rem;
    color: #ffffff;
    line-height: 1.6;
}

.disclaimer {
    color: #888899;
    font-size: 0.8rem;
    text-align: center;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# TITLE
# -----------------------------------

st.title("MOODMIRROR")

st.markdown(
    '<div class="subtitle">'
    'Take a photo and let AI estimate your facial expression.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------------
# CAMERA
# -----------------------------------

photo = st.camera_input("📸 Take a picture")


# -----------------------------------
# ANALYZE PHOTO
# -----------------------------------

if photo is not None:

    # Convert uploaded image into bytes
    image_bytes = photo.getvalue()

    # Convert bytes into an OpenCV image
    image_array = np.frombuffer(
        image_bytes,
        np.uint8
    )

    frame = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )

    # Analyze the image
    with st.spinner("🧠 Analyzing your expression..."):

        try:

            small_frame = cv2.resize(frame, (480, 360))
            
            result = DeepFace.analyze(
                small_frame,
                actions=["emotion"],
                detector_backend="retinaface",
                enforce_detection=True
                )

            emotion = result[0]["dominant_emotion"]

            confidence = result[0]["emotion"][emotion]

            recommendation = get_recommendation(emotion)


            # -----------------------------------
            # DISPLAY RESULT
            # -----------------------------------

            st.markdown(
                f"""
                <div class="result-box">

                <div class="emotion">
                😊 You look {emotion.upper()}
                </div>

                <p>
                Model confidence: {confidence:.1f}%
                </p>

                <hr>

                <h3>💡 TRY THIS</h3>

                <div class="recommendation">
                {recommendation}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        except Exception as error:

            st.error(
                "I couldn't analyze that photo. "
                "Try taking another one with better lighting."
            )


# -----------------------------------
# DISCLAIMER
# -----------------------------------

st.markdown(
    """
    <div class="disclaimer">
    MoodMirror estimates facial expression using AI.
    It does not diagnose emotions or mental-health conditions.
    </div>
    """,
    unsafe_allow_html=True
)