import cv2
from deepface import DeepFace
from recommendations import get_recommendation
import textwrap


# ---------------------------------------
# SETTINGS
# ---------------------------------------

WINDOW_NAME = "MoodMirror"

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not access camera.")
    exit()


# ---------------------------------------
# VARIABLES
# ---------------------------------------

mode = "camera"

emotion = ""
recommendation = ""
confidence = 0


# ---------------------------------------
# FUNCTION: DRAW TEXT
# ---------------------------------------

def draw_text_box(
    image,
    text,
    x,
    y,
    max_width=55,
    color=(255, 255, 255),
    font_size=0.6
):

    lines = textwrap.wrap(text, width=max_width)

    for line in lines:

        cv2.putText(
            image,
            line,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_size,
            color,
            1,
            cv2.LINE_AA
        )

        y += 30

    return y


# ---------------------------------------
# MAIN LOOP
# ---------------------------------------

while True:

    success, frame = camera.read()

    if not success:
        break


    # ===================================
    # CAMERA SCREEN
    # ===================================

    if mode == "camera":

        display = frame.copy()

        height, width = display.shape[:2]

        # Dark bottom panel
        cv2.rectangle(
            display,
            (0, height - 150),
            (width, height),
            (25, 25, 25),
            -1
        )

        # Title
        cv2.putText(
            display,
            "MOODMIRROR",
            (30, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.1,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # Subtitle
        cv2.putText(
            display,
            "Let's see what your expression says.",
            (30, height - 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (220, 220, 220),
            1,
            cv2.LINE_AA
        )

        # Button-like instruction
        cv2.rectangle(
            display,
            (30, height - 75),
            (300, height - 25),
            (80, 80, 80),
            -1
        )

        cv2.putText(
            display,
            "SPACE  •  SCAN MY MOOD",
            (45, height - 43),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1,
            cv2.LINE_AA
        )

        cv2.imshow(WINDOW_NAME, display)


    # ===================================
    # RESULT SCREEN
    # ===================================

    elif mode == "result":

        display = frame.copy()

        height, width = display.shape[:2]

        # Large result panel
        panel_top = height - 300

        cv2.rectangle(
            display,
            (0, panel_top),
            (width, height),
            (20, 20, 20),
            -1
        )

        # Header
        cv2.putText(
            display,
            "MOODMIRROR",
            (30, panel_top + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (180, 180, 180),
            1,
            cv2.LINE_AA
        )

        # Emotion
        emotion_display = emotion.upper()

        cv2.putText(
            display,
            f"YOU LOOK {emotion_display}",
            (30, panel_top + 85),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 255, 140),
            2,
            cv2.LINE_AA
        )

        # Confidence
        cv2.putText(
            display,
            f"Model confidence: {confidence:.1f}%",
            (30, panel_top + 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (180, 180, 180),
            1,
            cv2.LINE_AA
        )

        # Recommendation heading
        cv2.putText(
            display,
            "TRY THIS",
            (30, panel_top + 165),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 220, 255),
            2,
            cv2.LINE_AA
        )

        # Recommendation
        clean_recommendation = (
            recommendation
            .encode("ascii", "ignore")
            .decode()
        )

        draw_text_box(
            display,
            clean_recommendation,
            30,
            panel_top + 200,
            max_width=65,
            font_size=0.55
        )

        # Scan again
        cv2.putText(
            display,
            "SPACE  •  SCAN AGAIN       Q  •  EXIT",
            (width - 400, height - 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (150, 150, 150),
            1,
            cv2.LINE_AA
        )

        cv2.imshow(WINDOW_NAME, display)


    # ===================================
    # KEYBOARD
    # ===================================

    key = cv2.waitKey(1) & 0xFF


    # -----------------------------------
    # TAKE PHOTO
    # -----------------------------------

    if key == 32 and mode == "camera":

        captured_frame = frame.copy()

        # Show analyzing screen
        analyzing = captured_frame.copy()

        cv2.putText(
            analyzing,
            "ANALYZING...",
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 220, 255),
            2,
            cv2.LINE_AA
        )

        cv2.imshow(WINDOW_NAME, analyzing)

        cv2.waitKey(100)


        try:

            # Smaller image = faster processing
            small_frame = cv2.resize(
                captured_frame,
                (640, 480)
            )

            result = DeepFace.analyze(
                small_frame,
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]

            # Get confidence for the detected emotion
            confidence = result[0]["emotion"][emotion]

            # Get recommendation
            recommendation = get_recommendation(emotion)

            # Save captured frame
            frame = captured_frame

            # Switch to result screen
            mode = "result"


        except Exception:

            emotion = "unknown"
            confidence = 0
            recommendation = "Try taking another photo."

            frame = captured_frame
            mode = "result"


    # -----------------------------------
    # SCAN AGAIN
    # -----------------------------------

    elif key == 32 and mode == "result":

        mode = "camera"


    # -----------------------------------
    # QUIT
    # -----------------------------------

    elif key == ord("q"):

        break


# ---------------------------------------
# CLEAN UP
# ---------------------------------------

camera.release()
cv2.destroyAllWindows()