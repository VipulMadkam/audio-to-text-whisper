# 🎙️ Audio to Text using Whisper

A Python-based project that converts audio files into text using OpenAI Whisper, with audio preprocessing powered by FFmpeg.

---

## 🚀 Overview

This project takes an input audio file, processes it using FFmpeg for optimal speech recognition, and then converts it into text using a deep learning model.

It supports multilingual transcription (including Hindi) and is designed as a foundational step toward building a voice assistant system.

---

## ✨ Features

* 🎧 Audio preprocessing (resampling, mono conversion)
* 🧠 Speech-to-text using Whisper
* 🌍 Supports multiple languages (Hindi, English, etc.)
* ⚡ Clean and minimal output (no unnecessary logs)

---

## 🛠️ Tech Stack

* Python
* OpenAI Whisper
* FFmpeg
* PyTorch
* SpeechRecognition (for future real-time input)

---

## 📂 Project Structure

```
Chatbot/
│── Audio_to_Text.py
│── processed.wav
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/VipulMadkam/audio-to-text-whisper.git
cd audio-to-text-whisper
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Install FFmpeg (Required)

Download FFmpeg from the official website and add it to your system PATH.

---

## ▶️ Usage

Run the script:

```
python Audio_to_Text.py
```

---

## 📌 Example Output

```
Processing audio...
Recognized Text: sochati chalti batiya tip tip karte rahe...
```

---

## ⚠️ Notes

* Make sure your audio file path is correct in the script.
* FFmpeg must be installed and accessible via command line.
* For better accuracy, use larger Whisper models (`small`, `medium`).

---

## 🔥 Future Improvements

* 🎤 Real-time microphone input
* 🧠 AI-based response system (LLM integration)
* 🔊 Text-to-speech output
* 🤖 Full voice assistant (Jarvis-style system)

---

## 👨‍💻 Author

**Vipul Madkam**

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.
