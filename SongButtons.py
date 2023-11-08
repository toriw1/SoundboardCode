import os
import pygame
from pygame import mixer
import time

# Initialize the mixer
mixer.init()

# Replace with the relative folder path
music_folder_path = "Christmas Music WAV"

# Switch statements in Python to assign a song to a number 1 - 12
def switcher(argument):
    switcher = {
        1: "All I Want for Christmas Is You.wav",
        2: "Blue Christmas.wav",
        3: "Christmas (Baby Please Come Home).wav",
        4: "Here Comes Santa Claus.wav",
        5: "Holly Jolly Christmas.wav",
        6: "Ill Be Home for Christmas.wav",
        7: "Its Beginning to Look a Lot Like Christmas.wav",
        8: "Jingle Bell Rock.wav",
        9: "Last Christmas.wav",
        10: "Santa Claus Is Coming to Town.wav",
        11: "Santa Tell Me.wav",
        12: "Underneath the Tree.wav",
    }
    return switcher.get(argument, "Invalid song number")

# Give mp3 song name with keyboard input using the switcher function
song_number = int(input("Enter a song number: "))
song_name = switcher(song_number)
print(song_name)

def play_song(song_name):
    # Load the song from the switcher function
    song_path = "Christmas Music WAV/" + song_name
    mixer.music.load(song_path)
    mixer.music.play()

# Play the song until the user presses the stop button
play_song(song_name)
while True:
    print("Press 's' to stop the song")
    stop = input()
    if stop == "s":
        mixer.music.stop()
        break
    else:
        print("Invalid input")
        continue
    