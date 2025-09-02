import speech_recognition as sr

import webbrowser
import pyttsx3
from gtts import gTTS
import time
import os
import warnings
warnings.filterwarnings("ignore")
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello! This is a test.")
engine.runAndWait()


#Assistant voice
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()
    os.remove("voice.mp3")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language="ES")
    print(f'You say: {text} ')
    return text.lower()

try:
    speak("What is your name?")
    name = talk()
    greetings = f'Hi {name} nice to meet you'
    speak(greetings)
    print(greetings)
except:
        print("Sorry i don't understand.")
        quit()
speak(f'{name} say Amazon, Youtube or Google to automatically go to their respective pages')
print(f'{name} say Amazon, Youtube or Google to automatically go to their respective pages')
command = talk()

try:
    if 'amazon' in command:
        speak(f'{name} What product do you want to buy')
        text = talk()
        webbrowser.open(f'https://www.amazon.com.mx/{text}')

    elif 'youtube' in command:
        speak(f'{name} What video do you want to see')
        text = talk()
        webbrowser.open(f'https://www.youtube.com/results?search_query={text}')

    elif 'google' in command:
        speak(f'{name} What do you want to search')
        text = talk()
        webbrowser.open(f'https://www.google.com/search?client=firefox-b-d&q={text}')
except:
     print("I can't understand")
     quit()
