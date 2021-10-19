import smtplib

from Config.Config import config
from Functions.PlaySound import MidSound
from Functions.ProjectBase import speak, takeCommand


def Email():
    print("\33[93m" + "\33[1m" + "What is the message?" + "\33[0m" + "\n")
    speak("What is the message?")
    message = takeCommand()
    if message:
        speak("Please enter the receiver's email address.")
        Email_to = input("Receiver's Email: ")
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(str(config["Email"]), str(config["Password"]))
        smtp.sendmail(str(config["Email"]), Email_to, message)
        smtp.quit()
        print(
            "\33[92m"
            + "\33[1m"
            + f"\nSuccessfully sent a mail to {Email_to}"
            + "\33[0m"
            + "\n"
        )
        speak(f"Successfully sent a mail to {Email_to}")
        MidSound()
    else:
        Email()
