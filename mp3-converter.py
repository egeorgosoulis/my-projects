from pytube import YouTube
from pydub import AudioSegment


def download_and_convert_to_mp3(link):
    try:
        youtube_object = YouTube(link)
        video_stream = youtube_object.streams.filter(only_audio=True).first()
        video_stream.download()

        video_filename = video_stream.default_filename
        mp3_filename = video_filename.replace(".webm", ".mp3")

        audio = AudioSegment.from_file(video_filename, format="webm")
        audio.export(mp3_filename, format="mp3")
        
        return mp3_filename

    except Exception as e:  #
        print(f"Error: {e}")
        return None


def main():
    link = input("enter yt url: ")

    mp3_filename = download_and_convert_to_mp3(link)

    if mp3_filename:
        print(f"success")


if __name__ == "__main__":
    main()
