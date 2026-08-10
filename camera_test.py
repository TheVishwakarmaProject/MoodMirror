import cv2

# Load OpenCV's built-in face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open the Mac's camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("❌ Could not access the camera.")
    print("Check System Settings → Privacy & Security → Camera.")
    exit()

print("📷 Camera started!")
print("Press Q to quit.")

while True:
    # Read a frame from the camera
    success, frame = camera.read()

    if not success:
        print("❌ Could not read camera frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    # Draw a rectangle around every detected face
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face detected!",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Show the camera window
    cv2.imshow("MoodMirror - Camera Test", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
camera.release()
cv2.destroyAllWindows()

print("Camera closed.")