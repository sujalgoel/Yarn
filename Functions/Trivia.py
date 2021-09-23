import requests

from Functions.PlaySound import MidSound
from Functions.ProjectBase import speak, takeCommand


def Trivia():
    response = requests.get("https://fun-api.sujalgoel.engineer/trivia").json()

    answer = response["answer"]
    options = response["options"]
    question = response["question"]

    print("\33[93m" + "\33[1m" + question + "\33[0m")
    speak(question)
    for i in range(4):
        if i == 3:
            print(
                "\33[91m"
                + "\33[1m"
                + f"{str(i + 1)}) "
                + "\33[0m"
                + "\33[1m"
                + options[3]
                + "\33[0m"
                + "\n"
            )
            speak(f"or {options[3]}")
        else:
            print(
                "\33[91m"
                + "\33[1m"
                + f"{str(i + 1)}) "
                + "\33[0m"
                + "\33[1m"
                + options[i]
                + "\33[0m"
            )
            speak(options[i])
    userinput = takeCommand()
    if userinput:
        if answer.lower() == userinput.lower():
            print(
                "\33[92m"
                + "\33[1m"
                + f"You are correct! It was {answer}."
                + "\33[0m"
                + "\n"
            )
            speak(f"You are correct! It was {answer}.")
            MidSound()
        else:
            print(
                "\33[91m"
                + "\33[1m"
                + f"You are wrong! It was {answer}."
                + "\33[0m"
                + "\n"
            )
            speak(f"You are wrong! It was {answer}.")
            MidSound()
    else:
        Trivia()
