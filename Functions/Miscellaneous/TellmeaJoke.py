import time
import random
import pyjokes
import requests

from Functions.ProjectBase import speak
from Functions.PlaySound import LaughSound, MidSound


def TellmeaJoke():
    num = random.randint(1, 10)
    if num % 2 == 0:
        joke = pyjokes.get_joke()
        print("\33[1m" + "Joke: " + "\33[92m" + joke + "\33[0m" + "\n")
        speak(joke)
        LaughSound()
        MidSound()
    else:
        response = requests.get("https://fun-api.sujalgoel.engineer/joke").json()
        joke = response["joke"]
        punchline = response["punchline"]
        print("\33[1m" + "Joke: " + "\33[92m" + joke + "\33[0m")
        speak(joke)
        time.sleep(0.3)
        print("\33[1m" + "Punchline: " + "\33[92m" + punchline + "\33[0m" + "\n")
        speak(punchline)
        MidSound()
        LaughSound()
