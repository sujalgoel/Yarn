import os
import time
import requests
import youtube_dl
import urllib.request

from pydub import AudioSegment
from pydub.playback import play

from Functions.PlaySound import MidSound
from Functions.ProjectBase import speak, takeCommand


def YTDL(url, Title):
    class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    def my_hook(d):
        if d["status"] == "finished":
            print(
                "\33[93m"
                + "\33[1m"
                + "Playing "
                + "\33[0m"
                + "\33[92m"
                + "\33[1m"
                + Title
                + "\33[0m"
                + "\n"
            )
            speak(f"Playing {Title}")

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": "/Music/%(title)s.%(ext)s",
        "logger": MyLogger(),
        "progress_hooks": [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def PlaySong():
    print("\33[93m" + "\33[1m" + "What song do you want me to play?" + "\33[0m" + "\n")
    speak("What song do you want me to play?")
    song = takeCommand()
    if song:
        response = requests.get(
            f"https://fun-api.sujalgoel.engineer/ytsr?query={urllib.parse.quote(song)}"
        ).json()
        url = response["url"]
        Title = response["title"]
        FileExists = os.path.isfile("./Music/" + Title + ".mp3")
        FileName = f"{os.getcwd()}\Music\{Title}.mp3"
        if FileExists:
            print(
                "\33[93m"
                + "\33[1m"
                + "Playing "
                + "\33[0m"
                + "\33[92m"
                + "\33[1m"
                + Title
                + "\33[0m"
                + "\n"
            )
            speak(f"Playing {Title}")
            play(AudioSegment.from_mp3(FileName))
            time.sleep(0.5)
            MidSound()
        else:
            print(
                "\33[93m"
                + "\33[1m"
                + "Downloading "
                + "\33[0m"
                + "\33[92m"
                + "\33[1m"
                + Title
                + "\33[0m"
            )
            speak(f"Downloading {Title}")
            YTDL(url, Title)
            play(AudioSegment.from_mp3(FileName))
            time.sleep(0.5)
            MidSound()
    else:
        PlaySong()
