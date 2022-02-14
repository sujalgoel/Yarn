import requests

from Config.Config import config
from Functions.ProjectBase import speak
from Functions.PlaySound import MidSound


def GetAdvice():
    url = "https://api.sujalgoel.engineer/private/advice"
    advice = requests.get(url, headers={"User-agent": config["User-Agent"]}).json()[
        "advice"
    ]
    speak("Here is a piece of advice for you.")
    print("\33[1m" + "Advice: " + "\33[92m" + advice + "\33[0m" + "\n")
    speak(advice)
    MidSound()
