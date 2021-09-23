import random
import requests

from Functions.ProjectBase import speak
from Functions.PlaySound import MidSound


def GetQuote():
    num = random.randint(1, 10)
    response = requests.get("https://fun-api.sujalgoel.engineer/quote").json()
    quote = response["quote"]
    author = response["author"]
    if num % 2 == 0:
        print(
            "\33[1m"
            + "\33[92m"
            + quote
            + "\33[0m"
            + " - "
            + "\33[1m"
            + "\33[93m"
            + author
            + "\33[0m"
            + "\n"
        )
        speak(f"According to {author}, {quote}")
        MidSound()
    else:
        print(
            "\33[1m"
            + "\33[92m"
            + quote
            + "\33[0m"
            + " - "
            + "\33[1m"
            + "\33[93m"
            + author
            + "\33[0m"
            + "\n"
        )
        speak(f"{author} has rightly said, {quote}")
        MidSound()
