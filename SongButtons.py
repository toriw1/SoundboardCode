import os
import pygame
from pygame import mixer
import keyboard

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
        10: "Santa Claus Is Comin to Town.wav",
        11: "Santa Tell Me.wav",
        12: "Underneath the Tree.wav",
    }
    return switcher.get(argument, None)

# Give wav song name with keyboard input using the switcher function
song_number = int(input("Enter a song number: "))
song_name = switcher(song_number)
print(song_name)
        
# Play the initial song
if song_name is not None:
    song_path = os.path.join(music_folder_path, song_name)
    mixer.music.load(song_path)
    mixer.music.play()
    
while True:
    # if right arrow key is pressed, increment song number by 1
    if keyboard.is_pressed('right arrow'):
        song_number += 1
        song_name = switcher(song_number)
        if song_number > 12:
            song_number = 1
        if song_name is not None:
            print(song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    # if left arrow key is pressed, decrement song number by 1
    elif keyboard.is_pressed('left arrow'):
        song_number -= 1
        if song_number < 1:
            song_number = 12
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    # if s is pressed, stop the song
    elif keyboard.is_pressed('s'):
        mixer.music.stop()
        break
    else:
        continue