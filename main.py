# Regular Functions
from Functions.RPS import RPS
from Functions.GTP import GTP
from Functions.GTN import GTN
from Functions.Email import Email
from Functions.Greet import Greet
from Functions.Trivia import Trivia
from Functions.Weather import Weather
from Functions.PlaySong import PlaySong
from Functions.LieSwatter import LieSwatter
from Functions.YouTubePlay import YouTubePlay
from Functions.ProjectBase import takeCommand
from Functions.GoogleSearch import GoogleSearch
from Functions.YouTubeSearch import YouTubeSearch
from Functions.NewsHeadlines import NewsHeadlines

# Miscellaneous Functions
from Functions.Miscellaneous.Quit import Quit
from Functions.Miscellaneous.GetQuote import GetQuote
from Functions.Miscellaneous.GetAdvice import GetAdvice
from Functions.Miscellaneous.OpenGoogle import OpenGoogle
from Functions.Miscellaneous.PasswordGen import PasswordGen
from Functions.Miscellaneous.OpenYoutube import OpenYoutube
from Functions.Miscellaneous.CurrentTime import CurrentTime
from Functions.Miscellaneous.TellmeaJoke import TellmeaJoke
from Functions.Miscellaneous.SendWhatsappMsg import SendWhatsappMsg
from Functions.Miscellaneous.WikipediaSearch import WikipediaSearch



# Greet Function
Greet()

# Main Code
while True:

    try:

        query = takeCommand()

        if query:

            command = query.lower()

            if command:

                if "open google" in command:
                    try:
                        OpenGoogle()
                    except KeyboardInterrupt:
                        quit()

                elif "open youtube" in command:
                    try:
                        OpenYoutube()
                    except KeyboardInterrupt:
                        quit()

                elif "time" in command in command:
                    try:
                        CurrentTime()
                    except KeyboardInterrupt:
                        quit()

                elif "joke" in command:
                    try:
                        TellmeaJoke()
                    except KeyboardInterrupt:
                        quit()

                elif "search on google" in command:
                    try:
                        GoogleSearch()
                    except KeyboardInterrupt:
                        quit()

                elif "search on youtube" in command:
                    try:
                        YouTubeSearch()
                    except KeyboardInterrupt:
                        quit()

                elif "play on youtube" in command:
                    try:
                        YouTubePlay()
                    except KeyboardInterrupt:
                        quit()

                elif "generate a password" in command:
                    try:
                        PasswordGen()
                    except KeyboardInterrupt:
                        quit()

                elif "search on wikipedia" in command:
                    try:
                        WikipediaSearch()
                    except KeyboardInterrupt:
                        quit()

                elif "send a whatsapp message" in command:
                    try:
                        SendWhatsappMsg()
                    except KeyboardInterrupt:
                        quit()

                elif "news" in command:
                    try:
                        NewsHeadlines()
                    except KeyboardInterrupt:
                        quit()

                elif "weather" in command:
                    try:
                        Weather()
                    except KeyboardInterrupt:
                        quit()

                elif "play a song" in command:
                    try:
                        PlaySong()
                    except KeyboardInterrupt:
                        quit()

                elif "advice" in command:
                    try:
                        GetAdvice()
                    except KeyboardInterrupt:
                        quit()

                elif "quote" in command:
                    try:
                        GetQuote()
                    except KeyboardInterrupt:
                        quit()

                elif "rock paper and scissors" in command:
                    try:
                        RPS()
                    except KeyboardInterrupt:
                        quit()

                elif "guess the pokemon" in command:
                    try:
                        GTP()
                    except KeyboardInterrupt:
                        quit()

                elif "lie swatter" in command:
                    try:
                        LieSwatter()
                    except KeyboardInterrupt:
                        quit()

                elif "guess the number" in command:
                    try:
                        GTN()
                    except KeyboardInterrupt:
                        quit()

                elif "trivia" in command:
                    try:
                        Trivia()
                    except KeyboardInterrupt:
                        quit()

                elif "send an email" in command:
                    try:
                        Email()
                    except KeyboardInterrupt:
                        quit()

                elif "shutdown" in command:
                    try:
                        Quit()
                    except KeyboardInterrupt:
                        quit()

    except KeyboardInterrupt:
        quit()