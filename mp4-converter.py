from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from winsound import Beep


def Download(url, path):

    try:
        print("Downloading...")
        video = YouTube(url)
        video = video.streams.get_highest_resolution()
        video.download(path)
    except VideoUnavailable as e:
        print(f"Error : {e}")

    print(f"Video downloaded successfully to {path}")
    Beep(1200, 500)


url = input("Enter the YouTube URL of the video : ")
path = input("Enter the path to save the video : ")
Download(url, path)
