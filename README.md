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
## Running the program:
![image](https://github.com/user-attachments/assets/eb41dee8-980b-4f8e-b1d1-3836c5dd1807)
## Homepage:
![image](https://github.com/user-attachments/assets/1f786171-b594-4726-800a-271032db5858)
## Aadhar Upload:
![image](https://github.com/user-attachments/assets/6b59ae70-aff1-474b-985f-3ccb6cead948)
## DOB and Face extraction:
![image](https://github.com/user-attachments/assets/95775b79-18e2-49a1-b0f3-c04a28218f6f)

## Liveness check started by blink detection
![image](https://github.com/user-attachments/assets/56b0625b-c5bd-456e-9d80-5d74d745da66)
## Liveness check going on

![image](https://github.com/user-attachments/assets/88c53d2f-8492-4d08-a9df-4a3061f5a166)
## Capturing Selfie
![image](https://github.com/user-attachments/assets/51152ec1-f078-49f1-a096-b2cacdb24169)
## Face match confirmation
![image](https://github.com/user-attachments/assets/4b54f697-415e-46af-acc0-701f885696c2)
## Spoof Detection 
![image](https://github.com/user-attachments/assets/ab299945-7a90-4973-a52c-efc8e3000606)



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
