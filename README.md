# ✋ Real-Time Hand and Finger Counter

A robust real-time computer vision application designed to detect hands, track anatomical landmarks, and count extended fingers dynamically from a live video feed.

---

## 📌 Project Overview

The **Real-Time Hand and Finger Counter** leverages cutting-edge computer vision techniques to analyze live webcam input and determine the number of raised fingers on each hand. Powered by **OpenCV** and **MediaPipe Hands**, this application ensures high accuracy, low latency, and intuitive visual feedback — even with multiple hands in the frame.

---

## 🧠 Key Features

- 🤚 **Real-time finger counting** with high accuracy  
- ✌️ **Multi-hand detection** (supports both hands simultaneously)  
- 🔁 **Dynamic finger tracking** using anatomical landmarks  
- 👈 **Left/Right hand differentiation** for precise thumb detection  
- 💻 **Lightweight & efficient** — runs smoothly on CPU  

---

## 🛠️ Tech Stack

| Library       | Role                                  |
|---------------|---------------------------------------|
| Python        | Core programming language             |
| OpenCV        | Real-time video processing & display  |
| MediaPipe     | Hand tracking & landmark detection    |
| NumPy         | Efficient numerical computations      |

---

## 📷 Demo

> *Coming Soon*  


---

## 🧩 How It Works

1. **Video Feed Capture**  
   OpenCV initializes the webcam and captures frames in real time.

2. **Hand Detection & Landmark Mapping**  
   MediaPipe's `Hands` solution processes each frame, detecting hand presence and extracting 21 3D landmarks per hand.

3. **Finger State Analysis**  
   Landmark positions are analyzed to determine which fingers are extended, including special logic for thumb orientation and hand side (left/right).

4. **Overlay & Display**  
   The total number of raised fingers is drawn on the live video along with hand outlines and landmarks.

---

## 🧪 Usage Instructions

### 🔧 Prerequisites

- Python 3.7+
- Install required packages:
  ```bash
  pip install opencv-python mediapipe numpy
````

---

### ▶️ Run the App

```bash
python finger_counter.py
```

The webcam window will open, and the app will start counting your fingers in real-time!

---

## 📁 Project Structure

```
finger_counter/
│
├── finger_counter.py           # Main application script
├── HandTrackingModule.py       # Main Tracking module
├── requirements.txt            # Python dependencies (optional)
├── assets/                     # Screenshots, demo GIFs, etc.
└── README.md                   # Project overview
```

---

## 💡 Possible Enhancements

* 👆 Gesture recognition (e.g., "peace", "thumbs up")
* 🔊 Volume control using finger count
* 🧠 Sign language recognition as an extension
* 📲 Deploy on mobile using MediaPipe + Android/iOS SDK

---

## 🙏 Acknowledgements

* [MediaPipe](https://mediapipe.dev/) for robust hand tracking
* [OpenCV](https://opencv.org/) for real-time video processing

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🌟 Star This Repo

If you found this helpful or interesting, give it a ⭐ to support the project!

```

