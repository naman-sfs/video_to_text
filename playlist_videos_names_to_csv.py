'''
code to get all the videos of a youtube playlist
then add it in a scv file
'''
import os
import csv
from pytubefix import Playlist

# Step 1: Create or append to a CSV file
def write_videos_to_csv(playlist_url, csv_file):
    pl = Playlist(playlist_url)
    playlist_name = pl.title.replace(" ", "_")

    # Open the CSV file in append mode
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header only if the file does not exist
        if not file_exists:
            writer.writerow(["Playlist Name", "Video Number and Title"])
        
        # Write video details
        for i, video in enumerate(pl.videos, start=1):
            video_title = f"{i}. {video.title}"
            writer.writerow([playlist_name, video_title])
            print(f"Added '{video_title}' to CSV under playlist '{playlist_name}'")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    csv_file = "youtube_playlists.csv"  # Specify the CSV file name
    write_videos_to_csv(playlist_url, csv_file)
