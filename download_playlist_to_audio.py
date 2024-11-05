'''
Code to download the entire youtube playlist in the audio format
'''
import os
from pytubefix import Playlist

# Define paths
def create_folders(playlist_name):
    base_path = os.path.join(os.getcwd(), playlist_name)
    audio_folder = os.path.join(base_path, f"{playlist_name}-audio")

    os.makedirs(audio_folder, exist_ok=True)

    return audio_folder

# Step 1: Download audio from YouTube using pytubefix
def download_audio_from_playlist(playlist_url):
    pl = Playlist(playlist_url)
    playlist_name = pl.title.replace(" ", "_")
    audio_folder = create_folders(playlist_name)
    
    for i, video in enumerate(pl.videos, start=1):
        mp3_filename = f"{i}.{playlist_name}-audio.mp3"
        mp3_path = os.path.join(audio_folder, mp3_filename)

        # Check if the MP3 file already exists
        if os.path.exists(mp3_path):
            print(f"MP3 for video {i} already exists. Skipping download.")
        else:
            ys = video.streams.get_audio_only()
            ys.download(output_path=audio_folder, filename=mp3_filename)
            print(f"Downloaded audio as '{mp3_filename}'")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_audio_from_playlist(playlist_url)
