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
5. Run the script:
```bash
python3 motion_photo_telegram.py
```

---
> will make a detailed tutorial later. thank you.