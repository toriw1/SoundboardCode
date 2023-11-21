from tkinter import Tk, Label, Frame, LEFT, RIGHT

class SongGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Christmas Music Player")
        self.root.geometry("1024x600")
        self.root.configure(bg="green")

        # Create a frame to split the GUI
        frame_left = Frame(self.root, bg="green")
        frame_left.pack(side=LEFT, padx=20)

        frame_right = Frame(self.root, bg="green")
        frame_right.pack(side=RIGHT, padx=20)

        # Create a label to display song information
        self.song_info_label = Label(frame_right, text="Now Playing: None", font=("Helvetica", 12), bg="green", fg="white", anchor="e")
        self.song_info_label.pack(pady=20)

    def update_song_info(self, song_name):
        # Update the song information label
        self.song_info_label.config(text=f"Now Playing: {song_name}")

    def start_gui(self):
        # Run the Tkinter main loop
        self.root.mainloop()

if __name__ == "__main__":
    song_gui = SongGUI()
    song_gui.start_gui()
