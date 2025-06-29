# Aadhaar + Liveness + Face Verification System

A powerful desktop application built in **Python (Tkinter + OpenCV)** that performs:

✅ Aadhaar OCR  
✅ Age Verification  
✅ Liveness Check via Blink Detection  
✅ Spoof Detection on Selfie  
✅ Face Matching between Aadhaar and Selfie

 🎥 Webcam-powered. Uses image processing + ML for liveness and spoof detection.

---

## 🚀 Features

| Module | Description |
|--------|-------------|
| 🧾 **Aadhaar Upload** | Upload an image of Aadhaar (front side). |
| 🧠 **OCR + DOB Extraction** | Extracts text and detects Date of Birth from Aadhaar using OCR. |
| 🔞 **Age Verification** | Checks if user is **18+** based on DOB. |
| 👁️ **Liveness Check** | Detects **5 blinks live via webcam** to ensure person is real. |
| 🤳 **Selfie Capture** | Automatically captures a selfie after successful blink detection. |
| 🛡️ **Spoof Detection** | Checks for **screen/photo attacks** using blur + color variance. |
| 🧍‍♂️ **Face Matching** | Compares Aadhaar photo with selfie and shows similarity score. |

---

## 📸 Live Demo

> 📽️ [Watch Demo Video (YouTube)](https://example.com) *()*  


---

## 🧑‍💻 Tech Stack

- **Python 3.x**
- `Tkinter` – GUI
- `OpenCV` – Webcam + image processing
- `Pillow` – Image handling
- `PyTesseract` – OCR
- `face_recognition` – Face matching
- `NumPy`, `tflite_runtime` – Anti-spoofing model

---

## 📦 Installation Guide

> Works on **Windows**. No internet needed after build.  
> 🔒 Privacy-preserving: no data is stored or uploaded.



1. Clone the repo:

       git clone https://github.com/yourusername/aadhaar-liveness-verification
       cd aadhaar-liveness-verification
Create a virtual environment:


    python -m venv venv
    venv\Scripts\activate
    Install dependencies:


    pip install -r requirements.txt
Run the app:


    python main.py
