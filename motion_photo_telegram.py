from dotenv import load_dotenv
load_dotenv()
import RPi.GPIO as GPIO
import time
import os
import requests
from datetime import datetime

PIR_PIN = 17
LED_PIN = 27

save_dir = "/Path/to/your/photo/directory/" #make sure to use the full directory path.
os.makedirs(save_dir, exist_ok=True)

BOT_TOKEN = os.getenv("BOT_TOKEN") #check your bot id if it's right
CHAT_ID = os.getenv("CHAT_ID") #Same, double check both IDs.


def send_photo_to_telegram(image_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': CHAT_ID}
        response = requests.post(url, files=files, data=data)
        print("Telegram response:", response.status_code)


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.LOW)

print("Warming up PIR sensor")
time.sleep(5)
print("System ready. Monitoring for motion")


try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")

            GPIO.output(LED_PIN, GPIO.HIGH)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            image_path = os.path.join(save_dir, f"motion_{timestamp}.jpg")
            os.system(f"rpicam-still --vflip -o {image_path}")
            print(f"Photo saved: {image_path}")

            send_photo_to_telegram(image_path)

            time.sleep(3)

            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Interrupted. Cleaning up...")

finally:
    GPIO.cleanup()