from PIL import Image
import pytesseract
import requests
import pyautogui
import os
import time
import keyboard
import threading

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

biomes_ping = ["Hell", "Corruption", "Sand storm", "Starfall", "Null"]
biomes_noping = ["NORMAL", "Windy", "Snowy"]
webhook_url = "https://discord.com/api/webhooks/1302719341384700038/qp_pTHYEemyxMnusqOwdkvh4_9gU_quQ3NqFKX7-F8vqRbIoJTuSAQfThLpWAFaPhKiy"

user_id = 681934150743097387

current_biome = None

def detect():
    screenshot = pyautogui.screenshot("py\\biom.png", (5, 900, 160, 30))
    
    colors = [(53, 87, 114), (51, 114, 123)] #1 is rainy 2 is windy 3 normal 4 sandstorm 5 starfall 6 null 7 hell 8 corruption 9 snowy

    image = Image.open("py\\biom.png")
    text = pytesseract.image_to_string(image=image)
    for x in range(image.width):
            for y in range(image.height) :
                pixel = image.getpixel((x, y))[:3]
                if pixel == (103, 118, 106):
                        print("yes")


def webhook(url, biome, ping=False, glitched=False):
    if ping:
        data = {
            "content": f"{biome} detected, <@{user_id}>!"
        }
    elif glitched:
         data = {
            "content": f"Glitch Biome detected!!!, <@{user_id}>!"
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


time.sleep(2)
detect()
