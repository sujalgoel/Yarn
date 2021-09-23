import datetime

from Functions.ProjectBase import speak
from Functions.PlaySound import MidSound


def CurrentTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("\33[92m" + "\33[1m" + f"Sir the current time is {strTime}" + "\33[0m" + "\n")
    speak(f"Sir the current time is {strTime}")
    MidSound()