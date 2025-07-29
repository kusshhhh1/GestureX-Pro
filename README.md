# GestureX: AI-Powered Gesture-Based Control System

GestureX is a Python-based gesture recognition app that uses OpenCV and CVZone to detect hand gestures in real time and trigger actions like launching apps or managing AWS EC2 instances.

## 🔧 Features
- 1 Finger → Open Chrome 🌐
- 2 Fingers → Open Notepad 📝
- 3 Fingers → Open Spotify 🎵
- 4 Fingers → Launch AWS EC2 Instance ☁️
- 5 Fingers → Terminate AWS EC2 Instance ❌

## 🛠️ Tech Stack
- Python
- OpenCV
- CVZone (for hand detection)
- Boto3 (AWS EC2 control)

## 🚀 How to Run
1. Clone this repo
2. Make sure your webcam is connected
3. Run the script:
   ```bash
   python main.py
   ```
4. Show 1 to 5 fingers to your webcam and watch the magic happen!

## ⚠️ Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- cvzone (`pip install cvzone`)
- boto3 (`pip install boto3`)
- AWS credentials configured locally

## 📸 Demo
The camera window shows the number of fingers detected in real time. Use different hand gestures to trigger commands.

## 🧠 Built During
Internship Project under mentorship of Vimal Daga Sir

---
Made with ❤️ by Kushagra Sharma
