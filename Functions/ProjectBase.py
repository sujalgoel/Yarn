import pyttsx3
import speech_recognition as sr

from Functions.PlaySound import OpeningSound

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        OpeningSound()
        print("\33[31m" + "\33[1m" + "Listening..." + "\33[0m" + "\n")
        audio = speech.listen(source)
    try:
        query = speech.recognize_google(audio, language="en-in")
        print("\33[92m" + "\33[1m" + "You said: " + "\33[0m" + query + "\n")
    except Exception:
        query = None
    return query
