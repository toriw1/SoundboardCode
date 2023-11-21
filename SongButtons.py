import os
import pygame
from pygame import mixer
from pynput import keyboard

# Initialize the mixer
mixer.init()

# Replace with the relative folder path
music_folder_path = "Christmas Music WAV"

# Define song number
song_number = 0

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

def play_song(song_number):
    try:
        song_name = switcher(song_number)
        if song_name is not None:
            song_path = os.path.join(music_folder_path, song_name)
            mixer.music.load(song_path)
            mixer.music.play()
            # Print the song information after playing
            print(song_number, song_name)
    except pygame.error as e:
        print(f"An error occurred while trying to play the song: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def start_program():
    global song_number
    user_input = int(input("Enter a song number: "))
    
    # Adjust the initial value based on user input
    song_number = user_input
    
    with keyboard.Listener(on_press=on_press) as listener:
        # Print the initial song information
        play_song(song_number)  # Add 1 because your switcher function is 1-indexed
        listener.join()

 # Use arrow keys to change songs, accept input from number keys, and 's' to stop the music   
def on_press(key):
    global song_number
    if key == keyboard.Key.right:
        if song_number >= 12:
            song_number = 1
        else:
            song_number += 1
    elif key == keyboard.Key.left:
        if song_number <= 1:
            song_number = 12
        else:
            song_number -= 1
    if key == keyboard.KeyCode.from_char('1'):
        song_number = 1
    elif key == keyboard.KeyCode.from_char('2'):
        song_number = 2
    elif key == keyboard.KeyCode.from_char('3'):
        song_number = 3
    elif key == keyboard.KeyCode.from_char('4'):
        song_number = 4
    elif key == keyboard.KeyCode.from_char('5'):
        song_number = 5
    elif key == keyboard.KeyCode.from_char('6'):
        song_number = 6
    elif key == keyboard.KeyCode.from_char('7'):
        song_number = 7
    elif key == keyboard.KeyCode.from_char('8'):
        song_number = 8
    elif key == keyboard.KeyCode.from_char('9'):
        song_number = 9
    elif key == keyboard.KeyCode.from_char('10'):
        song_number = 10
    elif key == keyboard.KeyCode.from_char('11'):
        song_number = 11
    elif key == keyboard.KeyCode.from_char('12'):
        song_number = 12
    elif key == keyboard.KeyCode.from_char('s'):
        mixer.music.stop()
        return False  # Stop listener
    
    play_song(song_number)