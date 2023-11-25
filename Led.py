import time
import random 
from rpi_ws281x import *

class LEDController:
    def __init__(self, led_count=300, led_pin=18, led_brightness=65):
        # LED strip configuration
        self.LED_COUNT = led_count
        self.LED_PIN = led_pin
        self.LED_BRIGHTNESS = led_brightness

        # Initialize the library
        self.strip = Adafruit_NeoPixel(
            self.LED_COUNT, self.LED_PIN, 800000, 10, False, self.LED_BRIGHTNESS, 0
        )
        self.strip.begin()

    def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            if i % 2 == 0:
                self.strip.setPixelColor(i, Color(255, 0, 0))  # Red
            else:
                self.strip.setPixelColor(i, Color(0, 255, 0))  # Green

            self.strip.show()
            time.sleep(wait_ms / 1000.0)

    def theater_chase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
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

    def sparkle(self, density=0.4, duration=5):
        """Create an intense sparkle effect with varying blue tones."""
        start_time = time.time()

        while time.time() - start_time < duration:
            for i in range(self.strip.numPixels()):
                if random.random() < density:
                    blue_tone = random.randint(0, 255)
                    self.strip.setPixelColor(i, Color(0, 0, blue_tone))

            self.strip.show()
            time.sleep(0.04)

        self.turn_off_lights()
        
    def snow(self, wait_ms=50, iterations=5):
        """Simulate falling snow effect with continuous movement."""
        for _ in range(iterations):
            window = 3  # Size of the moving window
            for i in range(self.strip.numPixels() - window, -1, -1):
                # Reset the window by turning off all lights
                for j in range(i, i + window):
                    self.strip.setPixelColor(j, 0)

                # Turn on three lights in the window
                for j in range(i, i + window):
                    self.strip.setPixelColor(j, Color(255, 255, 255))  # White

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

    def color_blink(self, colors, wait_time, iterations=5):
        """Blink lights with specified colors at varying speeds."""
        for _ in range(iterations):
            # Blink the lights with all colors
            self.blink_all_colors(colors, wait_time)

            # Introduce a short delay between iterations
            time.sleep(0.05)

    def blink_all_colors(self, colors, wait_time):
        """Blink lights with all specified colors at the same time."""
        for i in range(self.strip.numPixels()):
            color = random.choice(colors)
            self.strip.setPixelColor(i, color)

        self.strip.show()
        time.sleep(wait_time)

        # Turn off all lights after blinking
        self.turn_off_lights()

    def christmas_twinkle(self, duration=10):
        """Create a twinkling effect with Christmas-themed colors."""
        start_time = time.time()

        while time.time() - start_time < duration:
            for i in range(self.strip.numPixels()):
                if random.random() < 0.1:  # Adjust the density of twinkling
                    color = random.choice([Color(255, 0, 0), Color(0, 255, 0), Color(255, 255, 255)])
                    self.strip.setPixelColor(i, color)

            self.strip.show()
            time.sleep(0.05)  # Adjust the speed of twinkling

        self.turn_off_lights()

    def winter_wonderland(self, density=0.1, duration=10):
        """Create a Winter Wonderland effect with falling snow and twinkling lights."""
        start_time = time.time()

        while time.time() - start_time < duration:
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

    def jingle_bells(self, wait_ms=50, iterations=10):
        """Simulate a Jingle Bells themed LED animation with continuous shifting movement."""
        for _ in range(iterations):
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

    def present(self, wait_ms=100, block_size=4):
        """Simulate a present-themed LED animation with red, yellow, and blue blocks moving in from the bottom,
        and green blocks moving in from the top, meeting in the middle."""
        colors = [
            Color(255, 0, 0),    # Red
            Color(0, 255, 0),    # Green
            Color(255, 255, 0),  # Yellow
            Color(0, 0, 255)     # Blue
        ]

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
            for i in range(j, j + block_size):
                self.strip.setPixelColor(i, colors[i % block_size])  # Move in from the bottom

            for i in range(self.strip.numPixels() - j - 1, self.strip.numPixels() - j - 1 - block_size, -1):
                self.strip.setPixelColor(i, colors[i % block_size])  # Move in from the top

            self.strip.show()
            time.sleep(wait_ms / 1000.0)

        for j in range(self.strip.numPixels() // 2 - 1, block_size - 1, -1):
            # Turn off the LEDs in the bottom half
            for i in range(self.strip.numPixels() - j - block_size, self.strip.numPixels() - j):
                self.strip.setPixelColor(i, Color(0, 0, 0))

            # Move the bottom color up
            for i in range(self.strip.numPixels() - j - block_size, self.strip.numPixels() - j):
                self.strip.setPixelColor(i, colors[i % block_size])

            self.strip.show()
            time.sleep(wait_ms / 1000.0)

        # Turn off all LEDs
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))

        self.strip.show()

    def santa(self, wait_ms=100):
        """Simulate a Santa-themed LED animation with alternating red and white blocks blinking across the strip."""
        colors = [
            Color(255, 0, 0),    # Red
            Color(255, 255, 255),  # White
        ]

        block_size = 4  # Adjust the block size as needed

        for _ in range(5):  # Adjust the number of blinks as needed
            for i in range(0, self.strip.numPixels(), block_size * len(colors)):
                for j in range(i, min(i + block_size, self.strip.numPixels())):
                    for color in colors:
                        self.strip.setPixelColor(j, color)
                        j += 1

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

            for i in range(0, self.strip.numPixels(), block_size * len(colors)):
                for j in range(i, min(i + block_size, self.strip.numPixels())):
                    self.strip.setPixelColor(j, Color(0, 0, 0))

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

        # Turn off all LEDs
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))

        self.strip.show()

    def cute_sparkle(self, colors, density=0.4, duration=10):
        """Create a cute sparkle effect with specified colors."""
        start_time = time.time()

        while time.time() - start_time < duration:
            for i in range(self.strip.numPixels()):
                if random.random() < density:
                    color = random.choice(colors)
                    self.strip.setPixelColor(i, color)

            self.strip.show()
            time.sleep(0.04)

        self.turn_off_lights()

    def festive_green(self, density=0.4, duration=10):
        """Create a Christmas-themed animation with falling snow and twinkling green lights."""
        start_time = time.time()

        while time.time() - start_time < duration:
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

    def turn_off_lights(self):
        """Turn off all lights."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()

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

            choice = input("Enter your choice: ")

            if choice == "1":
                led_controller.color_wipe(Color(255, 0, 0))  # Red color wipe
            elif choice == "2":
                led_controller.theater_chase(Color(127, 127, 127))  # White theater chase
            elif choice == "3":
                led_controller.sparkle()
            elif choice == "4":
                led_controller.snow()
            elif choice == "5":
                colors = [Color(255, 0, 0), Color(0, 255, 0), Color(255, 213, 0), Color(0, 0, 255)]
                wait_time = 0.3
                led_controller.color_blink(colors, wait_time)
            elif choice == "6":
                led_controller.christmas_twinkle()
            elif choice == "7":
                led_controller.winter_wonderland()
            elif choice == "8":
                for _ in range(10):
                    led_controller.jingle_bells()
            elif choice == "9":
                led_controller.present()
            elif choice == "10":
                led_controller.santa()
            elif choice == "11":
                cute_colors = [Color(255, 0, 25), Color(255, 255, 255), Color(255, 0, 183)]  # Red, White, Pink
                led_controller.cute_sparkle(cute_colors, density=0.4, duration=10)
            elif choice == "12":
                led_controller.festive_green()
            elif choice.lower() == "s":
                led_controller.turn_off_lights()
            elif choice.lower() == "q":
                break
            else:
                print("Invalid choice. Try again.")

    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        led_controller.turn_off_lights()  # Turn off LEDs when exiting"
