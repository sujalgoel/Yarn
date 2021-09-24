from Functions.ProjectBase import speak
from Functions.PlaySound import EndingSound
import sys


def Quit():
    print("\33[92m" + "\33[1m" + "Shutting Down." + "\33[0m")
    speak("Shutting Down.")
    EndingSound()
    sys.exit()
