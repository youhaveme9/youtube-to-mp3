# imports
from __future__ import unicode_literals
import youtube_dl
import os
import tkinter
from tkinter import *
from functools import partial
import pyautogui
from youtube_dl.utils import DownloadError

root = Tk()
def Download(url):
    global path
    global Url
    Url = url.get()
    # get present directory
    path = os.getcwd()
    try:
        song()
    except DownloadError as e:
        # song gets download but with an error
        '''
        raise PostProcessingError('ffprobe/avprobe and ffmpeg/avconv not found. Please install one.')
        youtube_dl.utils.PostProcessingError: ffprobe/avprobe and ffmpeg/avconv not found. Please install one.
        '''
        pyautogui.alert("Please Enter url")

def song():
    try:
        opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '1411',
                }],
                'extractaudio': True,
                'outtmpl': path + '/%(title)s.%(ext)s',
                'noplaylist': True
            }
        ydl1 = youtube_dl.YoutubeDL(opts)
        ydl1.download([Url])
    except Exception as e:
        pyautogui.alert("Download Complete")
        return
    

root.title("Youtube to MP3 downloader")
root.geometry("365x300")
l1 = Label(root, text="Welcome to Youtube to MP3 downloader", bg='pink').place(x=10, y=5)
url = StringVar()
l2 = Label(root, text="URL: ").place(x=20, y=50)
e1 = Entry(root, textvariable=url).place(x=95, y=50)
Download = partial(Download, url)
b1 = Button(root, text="Download", command=Download).place(x=105, y=80)

root.mainloop()