# 😊 MoodMirror

An AI-powered facial expression recognition and recommendation system.

## 🌟 About the Project

MoodMirror uses computer vision and deep learning to estimate a user's facial expression from a captured image and provide a small personalized recommendation based on the detected expression.

The project was created as a machine learning prototype demonstrating the integration of facial-expression recognition with an interactive user interface.

## ✨ Features

- 📸 Capture an image using the device camera
- 🧠 Facial-expression analysis using DeepFace
- 😊 Recognition of expressions such as:
  - Happy
  - Sad
  - Angry
  - Fear
  - Surprise
  - Disgust
  - Neutral
- 💡 Emotion-based recommendations
- 🌐 Interactive Streamlit web interface
- 📊 Displays the model's estimated confidence
- 🔄 Allows users to scan their expression again

## 🛠️ Technologies Used

- Python
- OpenCV
- DeepFace
- TensorFlow
- NumPy
- Streamlit

## 🧠 How It Works

```text
Camera
   ↓
Captured Image
   ↓
Face Detection
   ↓
DeepFace Emotion Analysis
   ↓
Estimated Facial Expression
   ↓
Recommendation Engine
   ↓
Personalized Suggestion
