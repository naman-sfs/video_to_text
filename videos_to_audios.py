import os
from moviepy.editor import VideoFileClip

# Function to convert video to audio
def video_to_audio(video_path, output_audio_path):
    clip = VideoFileClip(video_path)
    audio = clip.audio
    audio.write_audiofile(output_audio_path)

# Function to process videos in the AIT_Videos folder
def convert_videos_to_audio(videos_folder):
    for root, dirs, files in os.walk(videos_folder):
        for file in files:
            if file.endswith(('.mp4', '.mov', '.avi', '.mkv')):  # Add more video formats if needed
                video_path = os.path.join(root, file)
                audio_folder = root.replace('AIT_Videos', 'AIT_Audios')
                os.makedirs(audio_folder, exist_ok=True)

                # Replace spaces in the filename with underscores and change extension to .mp3
                audio_file_name = os.path.splitext(file)[0].replace(' ', '_') + '.mp3'
                audio_path = os.path.join(audio_folder, audio_file_name)

                # Convert video to audio
                video_to_audio(video_path, audio_path)
                print(f"Converted '{video_path}' to '{audio_path}'")

if __name__ == "__main__":
    videos_folder = "AIT_Videos"  # Path to the AIT_Videos folder
    convert_videos_to_audio(videos_folder)
