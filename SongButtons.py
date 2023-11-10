import os
import pygame
from pygame import mixer
from pynput import keyboard

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
        4: "Feliz Navidad.wav",
        5: "Here Comes Santa Claus.wav",
        6: "Holly Jolly Christmas.wav",
        7: "Ill Be Home for Christmas.wav",
        8: "Its Beginning to Look a Lot Like Christmas.wav",
        9: "Jingle Bell Rock.wav",
        10: "Last Christmas.wav",
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

 # Use arrow keys to change songs and 's' to stop the music   
def on_press(key):
    global song_number, song_name, song_path
    if key == keyboard.Key.right:
        song_number += 1
        song_name = switcher(song_number)
        if song_number >= 12:
            song_number = 0
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.Key.left:
        song_number -= 1
        if song_number < 1:
            song_number = 12
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    # Allow the user to also put input for song number while the music is playing
    elif key == keyboard.KeyCode.from_char('1'):
        song_number = 1
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('2'):
        song_number = 2
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('3'):
        song_number = 3
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('4'):
        song_number = 4
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('5'):
        song_number = 5
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('6'):
        song_number = 6
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()  
    elif key == keyboard.KeyCode.from_char('7'):
        song_number = 7
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path, song_name) 
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('8'):
        song_number = 8
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path,song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('9'):
        song_number = 9
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path,song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('10'):
        song_number = 10
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path,song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('11'):
        song_number = 11
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path,song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('12'):
        song_number = 12
        song_name = switcher(song_number)
        if song_name is not None:
            print(song_number, song_name)
            song_path = os.path.join(music_folder_path,song_name)
            mixer.music.load(song_path)
            mixer.music.play()
    elif key == keyboard.KeyCode.from_char('s'):
        mixer.music.stop()
        return False  # Stop listener
    

# Start the event listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()