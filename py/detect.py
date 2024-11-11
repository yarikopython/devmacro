from PIL import Image
import pytesseract
import requests
import pyautogui
import os
import time
import keyboard
import threading

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

biomes_ping = ["Hell", "Corruption", "Sandstorm", "Starfall", "Null"]
biomes_noping = ["Normal", "Windy", "Snowy"]
webhook_url = "https://discord.com/api/webhooks/1293885133165953034/egcgsKfawDe38louRl4u1A7FBJ3RNBaWCD2jiq3mIcR42mnhUz0abW2dZJN8ID_p3Hqt"

user_id = 681934150743097387

current_biome = None

def detect():
    screenshot = pyautogui.screenshot("py\\biom.png", (20, 945, 160, 30))
    
    image = Image.open("py\\biom.png")
    text = pytesseract.image_to_string(image=image)
    for biome in biomes_ping + biomes_noping:
        if biome in text:
            return biome
    return None

def webhook(url, biome, ping=False):
    if ping:
        data = {
            "content": f"{biome} detected, <@{user_id}>!"
        }
    else:
        
        data = {
            "content": f"New Biome detected: {biome}"
        }
    request = requests.post(url=url, json=data)


def check_biome():
    global current_biome
    new_biome = detect()
    if new_biome and new_biome != current_biome:
        if new_biome in biomes_ping:
            webhook(webhook_url, new_biome, ping=True)
        elif new_biome in biomes_noping:
            webhook(webhook_url, new_biome, ping=False)

            
        current_biome = new_biome
    time.sleep(5)


def start():
    thread = threading.Thread(target=check_biome)
    thread.daemon = True
    thread.start()
