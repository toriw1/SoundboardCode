import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
from pynput import keyboard

class SongGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.paused = False
        self.song_number = 1
        pygame.mixer.init()

        # Get the absolute path of the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Use the absolute path to construct the relative path to the image
        initial_image_path = os.path.join(script_dir, "GUIPictures/ChristmasBackground.png")

        self.image_path = initial_image_path
        self.load_image()

        self.panel = tk.Label(self, image=self.image)
        self.panel.image = self.image
        self.panel.pack()

        self.bind('<Key>', self.on_press)

    def load_image(self):
        image = Image.open(self.image_path)
        image = image.resize((1024, 600))
        self.image = ImageTk.PhotoImage(image)

    def update_image(self, new_image_path):
        self.image_path = new_image_path
        self.load_image()
        self.panel.configure(image=self.image)
        self.panel.image = self.image

    def switcher(self, argument):
        switcher = {
            1: ("All I Want for Christmas Is You.wav", "GUIPictures/All I Want for Christmas Is You.png"),
            2: ("Blue Christmas.wav", "GUIPictures/Blue Christmas.png"),
            3: ("Christmas (Baby Please Come Home).wav", "GUIPictures/Christmas (Baby Please Come Home).png"),
            4: ("Feliz Navidad.wav", "GUIPictures/Feliz Navidad.png"),
            5: ("Here Comes Santa Claus.wav", "GUIPictures/Here Comes Santa Claus.png"),
            6: ("Holly Jolly Christmas.wav", "GUIPictures/Holly Jolly Christmas.png"),
            7: ("Ill Be Home for Christmas.wav", "GUIPictures/Ill Be Home for Christmas.png"),
            8: ("Its Beginning to Look a Lot Like Christmas.wav", "GUIPictures/Its Beginning to Look a Lot Like Christmas.png"),
            9: ("Jingle Bell Rock.wav", "GUIPictures/Jingle Bell Rock.png"),
            10: ("Last Christmas.wav", "GUIPictures/Last Christmas.png"),
            11: ("Santa Tell Me.wav", "GUIPictures/Santa Tell Me.png"),
            12: ("Underneath the Tree.wav", "GUIPictures/Underneath the Tree.png"),
        }
        return switcher.get(argument, (None, None))

    def notify(self, *args, **kwargs):
        song_number = args[0]
        self.song_number = song_number
        self.play_song()

    def play_song(self):
        try:
            song_name, image_path = self.switcher(self.song_number)
            if song_name is not None:
                song_path = os.path.join("Christmas Music WAV", song_name)
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()

                # Print the song information after playing
                print(self.song_number, song_name)

                # Update the GUI
                self.update_image(image_path)
        except pygame.error as e:
            print(f"An error occurred while trying to play the song: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def on_press(self, event):
        if event.keysym == 'Right':
            self.song_number = (self.song_number % 12) + 1
        elif event.keysym == 'Left':
            self.song_number = (self.song_number - 2) % 12 + 1

        key = event.char

        if key.isdigit() and 1 <= int(key) <= 12:
            self.song_number = int(key)
        elif key.lower() == 's':
            pygame.mixer.music.stop()
            return False  # Stop listener
        else:
            # Check for individual keys using event.char
            if key == '1':
                self.song_number = 1
            elif key == '2':
                self.song_number = 2
            elif key == '3':
                self.song_number = 3
            elif key == '4':
                self.song_number = 4
            elif key == '5':
                self.song_number = 5
            elif key == '6':
                self.song_number = 6
            elif key == '7':
                self.song_number = 7
            elif key == '8':
                self.song_number = 8
            elif key == '9':
                self.song_number = 9
            elif key == '0':
                # Handle '0' as '10'
                self.song_number = 10
            elif key.lower() == 'a':
                # Handle 'a' as '11'
                self.song_number = 11
            elif key.lower() == 'b':
                # Handle 'b' as '12'
                self.song_number = 12

        # Play the song
        self.play_song()

if __name__ == "__main__":
    gui = SongGUI()
    gui.mainloop()