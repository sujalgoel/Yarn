import os
import time
import requests
import pyautogui

from Functions.ProjectBase import speak
from Functions.PlaySound import MidSound

MainDir = os.getcwd()


def GTP():
    response = requests.get("https://fun-api.sujalgoel.engineer/pokemon").json()

    HiddenImage = requests.get(response["data"]["HiddenImage"]).content
    HiddenImageFile = open(f"{MainDir}\\Images\\hidden-image.png", "wb")
    HiddenImageFile.write(HiddenImage)
    HiddenImageFile.close()

    os.startfile(f"{MainDir}\\Images\\hidden-image.png")
    print(
        "\33[93m"
        + "\33[1m"
        + "Opening the hidden image of the pokémon. You got 10 seconds!"
        + "\33[0m"
        + "\n"
    )
    speak("Opening the hidden image of the pokémon. You got 10 seconds!")

    t = 10
    while t > 0:
        speak(t)
        t -= 1
        time.sleep(1)

    pyautogui.hotkey("alt", "f4")

    speak("Now enter the pokemon name!")

    PokemonName = response["data"]["name"]
    UserInput = input("Enter the pokemon name: ")
    if UserInput:
        if UserInput.lower() == PokemonName.lower():
            print(
                "\33[92m"
                + "\33[1m"
                + f"\nIt was a {PokemonName}. You got it correct!"
                + "\33[0m"
                + "\n"
            )
            speak(f"It was a {PokemonName}. You got it correct!")
            ShowImage = requests.get(response["data"]["ShowImage"]).content
            ShowImageFile = open(f"{MainDir}\\Images\\show-image.png", "wb")
            ShowImageFile.write(ShowImage)
            ShowImageFile.close()
            os.startfile(f"{MainDir}\\Images\\show-image.png")
            time.sleep(3)
            pyautogui.hotkey("alt", "f4")
            MidSound()
        else:
            print(
                "\33[91m"
                + "\33[1m"
                + f"\nThe pokémon isn't {UserInput} but it was a {PokemonName}. You got it wrong!"
                + "\33[0m"
                + "\n"
            )
            speak(
                f"The pokémon isn't {UserInput} but it was a {PokemonName}. You got it wrong!"
            )
            ShowImage = requests.get(response["data"]["ShowImage"]).content
            ShowImageFile = open(f"{MainDir}\\Images\\show-image.png", "wb")
            ShowImageFile.write(ShowImage)
            ShowImageFile.close()
            os.startfile(f"{MainDir}\\Images\\show-image.png")
            time.sleep(3)
            pyautogui.hotkey("alt", "f4")
            MidSound()
    else:
        print(
            "\33[91m"
            + "\33[1m"
            + f"\nThe pokémon which I chose was a {PokemonName}."
            + "\33[0m"
            + "\n"
        )
        speak(f"The pokémon which I chose was a {PokemonName}.")
        ShowImage = requests.get(response["data"]["ShowImage"]).content
        ShowImageFile = open(f"{MainDir}\\Images\\show-image.png", "wb")
        ShowImageFile.write(ShowImage)
        ShowImageFile.close()
        os.startfile(f"{MainDir}\\Images\\show-image.png")
        time.sleep(3)
        pyautogui.hotkey("alt", "f4")
        MidSound()
