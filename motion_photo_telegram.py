import os
import time
import datetime
import requests
from dotenv import load_dotenv
import RPi.GPIO as GPIO

# Load bot token and chat ID from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Set up GPIO pins
PIR_PIN = 17     # PIR sensor output connected to GPIO 17 (physical pin 11)
LED_PIN = 27     # LED connected to GPIO 27 (physical pin 13)

GPIO.setmode(GPIO.BCM)        # Use BCM pin numbering
GPIO.setup(PIR_PIN, GPIO.IN)  # Set PIR as input
GPIO.setup(LED_PIN, GPIO.OUT) # Set LED as output

# Create the directory to save photos (if it doesn't exist)
photo_folder = "/your/path/to/photo/directory/alert-photos" # You can create this or just select a diretory.
os.makedirs(photo_folder, exist_ok=True)

def take_photo():
    """Capture a photo using the Pi Camera and return the full path."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_filename = f"motion_{timestamp}.jpg"
    image_path = os.path.join(photo_folder, image_filename)

    # Capture image using libcamera-still (non-GUI, fast, Pi OS supported)
    os.system(f"rpicam-still --vflip -o {image_path}")
    print(f"Photo saved: {image_path}")
    return image_path

def send_photo_to_telegram(image_path):
    """Send the photo to your Telegram account using the bot."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(image_path, 'rb') as photo:
            files = {'photo': photo}
            data = {'chat_id': CHAT_ID}
            response = requests.post(url, files=files, data=data)
            if response.status_code == 200:
                print("Photo sent to Telegram")
            else:
                print(f"Telegram error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error sending photo: {e}")

# Start the program
print("Warming up PIR sensor...")
time.sleep(5)
print("System ready. Monitoring for motion...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")

            # Turn on LED
            GPIO.output(LED_PIN, GPIO.HIGH)

            # Take photo
            image_path = take_photo()

            # Send photo via Telegram
            send_photo_to_telegram(image_path)

            # Wait 3 seconds before resuming
            time.sleep(3)

            # Turn off LED
            GPIO.output(LED_PIN, GPIO.LOW)

        else:
            time.sleep(0.1)  # Sleep briefly to avoid high CPU usage

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    GPIO.cleanup()
