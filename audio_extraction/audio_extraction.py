import moviepy.editor as mp
import os

path=input("Enter the path")

videoClip=mp.VideoFileClip(path)
audioClip=videoClip.audio
audioClip.write_audiofile("audio.mp3")