from pytube import YouTube
import moviepy.editor as mp
import os

readme = print("Penser à lire le readme !/ Remember to read the readme !")
video_url = str(input("Insert YouTube video link/Insérer le lien d'une vidéo YouTube : "))

yt = YouTube(video_url)
video = yt.streams.filter(only_audio=True).first()
author = str(input("Auteur/Author : "))
name = str(input("Nom de la musique/Name of music : "))
composition = author + "-" + name

file_path = os.path.join("C:/Users/<Username>/Download", video.default_filename)
video.download("C:/Users/lilia/Music/New")

clip = mp.AudioFileClip(file_path)
new_file_path = os.path.join("C:/Users/<Username>/Download", composition + ".mp3")
clip.write_audiofile(new_file_path)

os.remove(file_path)
