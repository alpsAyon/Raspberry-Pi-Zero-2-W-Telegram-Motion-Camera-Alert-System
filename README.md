## 🔔 Raspberry Pi Zero 2 W Telegram Motion Camera Alert System

This IoT project uses a PIR motion sensor and Pi Camera to capture and send motion-triggered photos to a Telegram bot. Useful for DIY home security setups.

---
### 📦 Features:
* Detects motion using a PIR sensor
* Takes timestamped photo using Raspberry Pi Camera
* Sends photo instantly to Telegram via a bot
* LED indicator for motion status
* Easily customizable and extendable
---

## 🧰 Components Used

| Component             | Description                  |
|----------------------|------------------------------|
| Raspberry Pi Zero 2 W | With RPi Camera enabled      |
| HC-SR501 PIR Sensor   | Motion detection             |
| LED                   | Motion visual indicator      |
| 330Ω Resistor         | In series with LED           |
| Pi Camera Module      | Captures motion-triggered image |
| Jumper Wires + Breadboard | Standard wiring tools     |

---

## 🧠 How It Works

1. Sensor warms up for 5 seconds
2. If motion is detected:
   - LED turns on
   - A photo is captured using the Pi Camera
   - Photo is sent to your Telegram account
3. After 3 seconds, LED turns off and system resumes monitoring

---

## 🔧 Raspberry Pi GPIO Wiring

| Component | Pi GPIO (BCM) | Physical Pin |
|-----------|----------------|--------------|
| PIR OUT   | GPIO17         | Pin 11       |
| LED +     | GPIO27         | Pin 13       |
| LED - (via 330Ω) | GND       | Pin 9        |
| PIR VCC   | 3.3V           | Pin 1        |
| PIR GND   | GND            | Pin 6        |

---

###📘 Overview of the System
This project continuously monitors a room using a PIR (Passive Infrared) motion sensor. When motion is detected:

An LED is turned on to signal detection.

The Pi Camera takes a photo and saves it locally.

The photo is then sent directly to your Telegram account using a bot you created.

### 🛠️ Setup
1. Create a Telegram bot using @BotFather

2. Get your chat ID via @JsonDumpCUBot

3. Create a .env file with:
```bash
BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
```
4. Install dependencies:
```bash
pip3 install -r requirements.txt
```

or you could install them running the following commands.
```bash
sudo apt update
sudo apt install libraspberrypi-bin python3-pip
pip3 install -r requirements.txt
```

5. Run the script:
```bash
python3 motion_photo_telegram.py
```

---
> will make a detailed tutorial later. thank you.