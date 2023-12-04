import time
import random
from rpi_ws281x import *
import keyboard
import threading

class LEDController:
    # Add these constants for special keys
    LED_OFF = -1
    QUIT = -2
    INCREMENT = -3
    DECREMENT = -4

    def __init__(self, led_count=300, led_pin=18, led_brightness=50):
        # LED strip configuration
        self.LED_COUNT = led_count
        self.LED_PIN = led_pin
        self.LED_BRIGHTNESS = led_brightness

        # Initialize the library
        self.strip = Adafruit_NeoPixel(
            self.LED_COUNT, self.LED_PIN, 800000, 10, False, self.LED_BRIGHTNESS, 0
        )
        self.strip.begin()

        # Initialize animation control attributes
        self.current_animation_thread = None
        self.stop_animation = False
        self.animation_lock = threading.Lock()

        self.animation_choice = 1  # Initialize with the first animation

    def run_animation_by_choice(self, animation_choice):
        with self.animation_lock:
            # If there's a running animation thread, stop it
            if self.current_animation_thread and self.current_animation_thread.is_alive():
                self.stop_animation = True
                self.current_animation_thread.join()

            animation_function, animation_params = self.switcher(animation_choice)

            try:
                while not self.stop_animation:
                    self.turn_off_lights()

                    if animation_function is not None:
                        animation_function(*animation_params)

            except KeyboardInterrupt:
                print("\nExiting.")
            finally:
                self.turn_off_lights()
                self.stop_animation = False

    def run_led(self):
        while True:
            if keyboard.is_pressed('1') or keyboard.is_pressed('2') or keyboard.is_pressed('3') \
                    or keyboard.is_pressed('4') or keyboard.is_pressed('5') or keyboard.is_pressed('6') \
                    or keyboard.is_pressed('7') or keyboard.is_pressed('8') or keyboard.is_pressed('9') \
                    or keyboard.is_pressed('0') or keyboard.is_pressed('a') or keyboard.is_pressed('b') \
                    or keyboard.is_pressed('s'):
                key_str = keyboard.read_event(suppress=True).name  # Use event.name to get the key name

                if key_str.isdigit() and 1 <= int(key_str) <= 9:
                    animation_choice = int(key_str)
                elif key_str.isdigit() and key_str == '0':
                    animation_choice = 10
                elif key_str.lower() == 'a':
                    animation_choice = 11
                elif key_str.lower() == 'b':
                    animation_choice = 12
                else:
                    print("Invalid choice. Try again.")
                    time.sleep(0.1)  # Add a short delay
                    continue

                self.stop_animation = False
                # Stop the current animation thread if running
                if self.current_animation_thread and self.current_animation_thread.is_alive():
                    self.stop_animation = True
                    self.current_animation_thread.join()

               # Run the corresponding LED animation based on new_choice in a separate thread
                animation_thread = threading.Thread(target=self.run_animation_by_choice, args=(animation_choice,))
                animation_thread.start()
                self.current_animation_thread = animation_thread

            time.sleep(0.1)  # Add a short delay to avoid rapid key presses


    def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            if i % 2 == 0:
                self.strip.setPixelColor(i, Color(255, 0, 0))  # Red
            else:
                self.strip.setPixelColor(i, Color(0, 255, 0))  # Green

            self.strip.show()
            time.sleep(wait_ms / 1000.0)

            # Check for keyboard input or stop signal
            if self.stop_animation:
                break

    def theater_chase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            if self.stop_animation:  # Check for interruption
                break

            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    if q == 0:
                        self.strip.setPixelColor(i + q, color)
                    elif q == 1:
                        self.strip.setPixelColor(i + q, Color(252, 129, 248))  # Light Pink
                    else:
                        self.strip.setPixelColor(i + q, 0)

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)

                if self.stop_animation:  # Check for interruption
                    break

    def sparkle(self, density=0.4, duration=5):
        """Create an intense sparkle effect with varying blue tones."""
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.stop_animation:  # Check for interruption
                break

            for i in range(self.strip.numPixels()):
                if random.random() < density:
                    blue_tone = random.randint(0, 255)
                    self.strip.setPixelColor(i, Color(0, 0, blue_tone))

            self.strip.show()
            time.sleep(0.04)

        self.turn_off_lights()

    def snow(self, wait_ms=50, iterations=5):
        """Simulate falling snow effect with continuous movement."""
        window = 3  # Size of the moving window

        for _ in range(iterations):
            if self.stop_animation:  # Check for interruption
                break

            for i in range(self.strip.numPixels() - window, -1, -1):
                # Reset the window by turning off all lights
                for j in range(i, i + window):
                    self.strip.setPixelColor(j, 0)

                # Turn on three lights in the window
                for j in range(i, i + window):
                    self.strip.setPixelColor(j, Color(255, 255, 255))  # White

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

                if self.stop_animation:  # Check for interruption
                    break

            # Reset the strip by turning off all lights
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, 0)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)

    def color_blink(self, colors, wait_time, iterations=5):
        """Blink lights with specified colors at varying speeds."""
        for _ in range(iterations):
            if self.stop_animation:  # Check for interruption
                break

            # Blink the lights with all colors
            self.blink_all_colors(colors, wait_time)

            # Introduce a short delay between iterations
            time.sleep(0.05)

            if self.stop_animation:  # Check for interruption
                break

    def blink_all_colors(self, colors, wait_time):
        """Blink lights with all specified colors at the same time."""
        for i in range(self.strip.numPixels()):
            if self.stop_animation:  # Check for interruption
                break

            color = random.choice(colors)
            self.strip.setPixelColor(i, color)

        self.strip.show()
        time.sleep(wait_time)

        # Turn off all lights after blinking
        self.turn_off_lights()

        if self.stop_animation:  # Check for interruption
            return

    def christmas_twinkle(self, duration=10):
        """Create a twinkling effect with Christmas-themed colors."""
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.stop_animation:  # Check for interruption
                break

            for i in range(self.strip.numPixels()):
                if random.random() < 0.1:  # Adjust the density of twinkling
                    color = random.choice([Color(255, 0, 0), Color(0, 255, 0), Color(255, 255, 255)])
                    self.strip.setPixelColor(i, color)

            self.strip.show()
            time.sleep(0.05)  # Adjust the speed of twinkling

        self.turn_off_lights()

        if self.stop_animation:  # Check for interruption
            return

    def winter_wonderland(self, density=0.1, duration=10):
        """Create a Winter Wonderland effect with falling snow and twinkling lights."""
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.stop_animation:  # Check for interruption
                break

            # Simulate falling snow
            for i in range(self.strip.numPixels()):
                if random.random() < density:
                    self.strip.setPixelColor(i, Color(255, 255, 255))  # White

            # Twinkle lights like stars
            for i in range(self.strip.numPixels()):
                if random.random() < 0.09:  # Adjust the density for twinkling effect
                    twinkle_color = Color(
                        random.randint(100, 255),
                        random.randint(100, 255),
                        random.randint(100, 255),
                    )
                    self.strip.setPixelColor(i, twinkle_color)

            self.strip.show()
            time.sleep(0.04)

        self.turn_off_lights()

        if self.stop_animation:  # Check for interruption
            return

    def jingle_bells(self, wait_ms=50, iterations=10):
        """Simulate a Jingle Bells themed LED animation with continuous shifting movement."""
        for _ in range(iterations):
            if self.stop_animation:  # Check for interruption
                break

            # Shift all LEDs to the right by 1 pixel
            last_color = self.strip.getPixelColor(self.strip.numPixels() - 1)
            for i in range(self.strip.numPixels() - 1, 0, -1):
                self.strip.setPixelColor(i, self.strip.getPixelColor(i - 1))

            self.strip.setPixelColor(0, last_color)  # Move the last LED color to the first LED

            # Set colors to only yellow, gold, and red
            colors = [
                Color(255, 213, 0),  # Yellow
                Color(255, 153, 0),  # Yellow/Orange
                Color(255, 0, 0),    # Red
            ]
            random.shuffle(colors)

            for i in range(self.strip.numPixels()):
                if random.choice([True, False]):
                    self.strip.setPixelColor(i, Color(0, 0, 0))  # Turn off
                else:
                    # Set a shuffled random color from yellow, gold, or red
                    color = colors[i % len(colors)]
                    self.strip.setPixelColor(i, color)

            # Display the updated LED colors
            self.strip.show()
            time.sleep(wait_ms / 1500.0)

            # Turn off the last LED to create a continuous shifting effect
            self.strip.setPixelColor(self.strip.numPixels() - 1, Color(0, 0, 0))

            if self.stop_animation:  # Check for interruption
                break

    def present(self, wait_ms=100, block_size=4, iterations=5):
        """Simulate a present-themed LED animation with red, yellow, and blue blocks moving in from the bottom,
        and green blocks moving in from the top, meeting in the middle."""
        colors = [
            Color(255, 0, 0),    # Red
            Color(0, 255, 0),    # Green
            Color(255, 255, 0),  # Yellow
            Color(0, 0, 255)     # Blue
        ]

        for _ in range(iterations):
            if self.stop_animation:  # Check for interruption
                break

            # Set initial colors for each LED based on their position
            for i in range(self.strip.numPixels()):
                if i < self.strip.numPixels() // 2:
                    self.strip.setPixelColor(i, Color(0, 0, 0))  # Clear for the top half
                else:
                    self.strip.setPixelColor(i, Color(0, 0, 0))  # Turn off the bottom half

            self.strip.show()
            time.sleep(wait_ms / 1000.0)

            # Move in from the bottom and top simultaneously
            for j in range(self.strip.numPixels() // 2):
                if self.stop_animation: # Check for interruption
                    break

                for i in range(j, j + block_size):
                    self.strip.setPixelColor(i, colors[i % block_size])  # Move in from the bottom

                for i in range(self.strip.numPixels() - j - 1, self.strip.numPixels() - j - 1 - block_size, -1):
                    self.strip.setPixelColor(i, colors[i % block_size])  # Move in from the top

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

            # Clear the strip by turning off all lights
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, 0)

            self.strip.show()
            time.sleep(wait_ms / 1000.0)

        # Clear the remaining present pixels
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, 0)

        self.strip.show()

        if self.stop_animation:  # Check for interruption
            return

    def santa(self, wait_ms=100):
        """Simulate a Santa-themed LED animation with alternating red and white blocks blinking across the strip."""
        colors = [
            Color(255, 0, 0),    # Red
            Color(255, 255, 255),  # White
        ]

        block_size = 4  # Adjust the block size as needed

        for _ in range(5):  # Adjust the number of blinks as needed
            if self.stop_animation:  # Check for interruption
                break

            for i in range(0, self.strip.numPixels(), block_size * len(colors)):
                if self.stop_animation:  # Check for interruption
                    break

                for j in range(i, min(i + block_size, self.strip.numPixels())):
                    for color in colors:
                        self.strip.setPixelColor(j, color)
                        j += 1

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

            for i in range(0, self.strip.numPixels(), block_size * len(colors)):
                if self.stop_animation:  # Check for interruption
                    break

                for j in range(i, min(i + block_size, self.strip.numPixels())):
                    self.strip.setPixelColor(j, Color(0, 0, 0))

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

        # Turn off all LEDs
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))

        self.strip.show()

        if self.stop_animation:  # Check for interruption
            return

    def cute_sparkle(self, colors, density=0.4, duration=10):
        """Create a cute sparkle effect with specified colors."""
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.stop_animation:  # Check for interruption
                    break
            
            for i in range(self.strip.numPixels()):
                if random.random() < density:
                    color = random.choice(colors)
                    self.strip.setPixelColor(i, color)

            self.strip.show()
            time.sleep(0.04)

        self.turn_off_lights()

        if self.stop_animation:  # Check for interruption
            return

    def festive_green(self, density=0.4, duration=10):
        """Create a Christmas-themed animation with falling snow and twinkling green lights."""
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.stop_animation:  # Check for interruption
                break

            # Simulate falling snow
            for i in range(self.strip.numPixels()):
                if random.random() < density:
                    self.strip.setPixelColor(i, Color(255, 255, 255))  # White

            # Twinkle lights like stars
            for i in range(self.strip.numPixels()):
                if random.random() < 0.38:  # Adjust the density for twinkling effect
                    twinkle_color = Color(8, 64, 7)  # Dark Green
                    self.strip.setPixelColor(i, twinkle_color)

            self.strip.show()
            time.sleep(0.08)

        self.turn_off_lights()

        if self.stop_animation:  # Check for interruption
            return

    def turn_off_lights(self):
        """Turn off all lights."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()

    def switcher(self, argument):
        switcher = {
            1: (self.color_wipe, (Color(255, 0, 0),)),
            2: (self.sparkle, ()),
            3: (self.festive_green, ()),
            4: (self.color_blink, ([Color(255, 0, 0), Color(0, 255, 0), Color(255, 213, 0), Color(0, 0, 255)], 0.3)),
            5: (self.santa, ()),
            6: (self.christmas_twinkle, ()),
            7: (self.winter_wonderland, ()),
            8: (self.snow, ()),
            9: (self.jingle_bells, ()),
            10: (self.theater_chase, (Color(127, 127, 127),)),
            11: (self.cute_sparkle, ([Color(255, 0, 25), Color(255, 255, 255), Color(255, 0, 183)], 0.4, 10)),
            12: (self.present, ()),
        }
        return switcher.get(argument, (None, None))

    def on_press(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            if event.is_keypad or len(event.name) > 1:
                key = event.name
            else:
                key = event.char

            if key.isdigit() and 0 <= int(key) <= 9:
                self.animation_choice = int(key)
            elif key.lower() == 'a':
                self.animation_choice = 11
            elif key.lower() == 'b':
                self.animation_choice = 12
            else:
                print("Invalid choice. Try again.")
                return

            self.stop_animation = True
            if self.current_animation_thread is not None and self.current_animation_thread.is_alive():
                self.current_animation_thread.join()

            self.current_animation_thread = threading.Thread(target=self.run_animation_by_choice, args=(self.animation_choice,))
            self.current_animation_thread.start()

if __name__ == "__main__":
    led_controller = LEDController()

    try:
        while True:
            print("Press a key to trigger LED dances:")
            print("1: Color Wipe")
            print("2: Theater Chase")
            print("3: Sparkle")
            print("4: Snow")
            print("5: Color Blink")
            print("6: Christmas Twinkle")
            print("7: Winter Wonderland")
            print("8: Jingle Bells")
            print("9: Present Animation")
            print("10: Santa Animation")
            print("11: Cute Sparkle")
            print("12: Festive Green")
            print("s: Turn Off Lights")
            print("Q: Quit")

            led_controller.run_led()

    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        led_controller.turn_off_lights()
