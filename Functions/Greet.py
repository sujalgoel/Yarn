import datetime

from Functions.ProjectBase import speak
from Functions.PlaySound import OpeningSound, MidSound


def Greet():
    hour = datetime.datetime.now().hour
    greetings = ""

    OpeningSound()

    if 5 >= hour < 12:
        greetings = "Good morning sir!"

    elif 12 >= hour < 18:
        greetings = "Good afternoon sir!"

    else:
        greetings = "Good evening sir!"

    greetings += "\nI am Yarn 🧶, your virtual assistant! How may I help you?"

    print("\33[92m" + "\33[1m" + greetings + "\33[0m" + "\n")
    speak(greetings)
    MidSound()
