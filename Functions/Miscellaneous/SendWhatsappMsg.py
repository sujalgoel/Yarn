import webbrowser
import urllib.parse

from Functions.PlaySound import MidSound
from Functions.ProjectBase import speak, takeCommand


def SendWhatsappMsg():
    print("\33[93m" + "\33[1m" + "What is the message?" + "\33[0m" + "\n")
    speak("What is the message?")
    message = takeCommand()
    if message:
        webbrowser.open(
            f"https://web.whatsapp.com/send?&text={urllib.parse.quote(message)}"
        )
        speak("Sending message on whatsapp.")
        MidSound()
    else:
        SendWhatsappMsg()
