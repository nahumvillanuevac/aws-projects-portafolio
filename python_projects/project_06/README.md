# Voice Assistant with Python

## Description
This is a simple voice assistant program in Python that uses speech recognition and text-to-speech to interact with the user. It can open Amazon, YouTube, or Google search pages based on voice commands.

---

## Features

- Uses microphone input to recognize speech.
- Speaks back to the user using Google's Text-to-Speech (`gTTS`) and `pygame` for audio playback.
- Recognizes commands to open Amazon, YouTube, or Google search.
- Handles basic conversation like asking the user’s name and responding with greetings.

---

## Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `gTTS`
  - `pygame`
  - `webbrowser` (built-in)

Install required packages with:

```bash
pip install SpeechRecognition pyttsx3 gTTS pygame
```