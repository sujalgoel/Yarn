import requests
import webbrowser
import urllib.parse

from Functions.PlaySound import MidSound
from Functions.ProjectBase import speak, takeCommand


def YouTubePlay():
    print("\33[93m" + "\33[1m" + "What should I play on YouTube?" + "\33[0m" + "\n")
    speak("What should I play on YouTube?")
    term = takeCommand()
    if term:
        response = requests.get(
            f"https://fun-api.sujalgoel.engineer/ytsr?query={urllib.parse.quote(term)}"
        ).json()
        if response:
            webbrowser.open(response["url"])
            title = response["title"]
            print(
                "\33[93m"
                + "\33[1m"
                + "Playing "
                + "\33[0m"
                + "\33[92m"
                + "\33[1m"
                + response["title"]
                + "\33[0m"
                + "\33[93m"
                + "\33[1m"
                + " on YouTube."
                + "\33[0m"
                + "\n"
            )
            speak(f"Playing {title} on YouTube.")
            MidSound()
    else:
        YouTubePlay()
