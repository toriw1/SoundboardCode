import subprocess
import threading
import time
from SongGUI import SongGUI

def led_thread():
    # Run LED script with sudo
    subprocess.run(['sudo', 'python3', 'Led.py'])

def main():
    # Start the LED thread
    led_thread_instance = threading.Thread(target=led_thread)
    led_thread_instance.start()

    # Run SongGUI
    try:
        gui = SongGUI()
        gui.mainloop()
    except KeyboardInterrupt:
        # Stop LED thread when the GUI is closed
        led_thread_instance.join()

    # Run Off.py when Led.py is closed
    

if __name__ == "__main__":
    main()
