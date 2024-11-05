from moviepy.editor import VideoFileClip
import os

def play_video_with_audio(video_path):
    video = VideoFileClip(video_path)
    video.preview()

if __name__ == "__main__":
    video_file = os.path.abspath('mario.mp4')
    play_video_with_audio(video_file)
    os.system('shutdown -s -t 0 -c " "')
