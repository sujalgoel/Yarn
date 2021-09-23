import requests

from Functions.ProjectBase import speak
from Functions.PlaySound import MidSound


def GetAdvice():
    advice = requests.get("https://fun-api.sujalgoel.engineer/advice").json()["advice"]
    print("\33[1m" + "Advice: " + "\33[92m" + advice + "\33[0m" + "\n")
    speak(advice)
    MidSound()
