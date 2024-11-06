from macro import Collection
import os
import requests
import keyboard
from pyrobloxbot import NoRobloxWindowException
import pyautogui
import time

vip = False
running = False


def settings():
    global vip
    global auraforequip
        
    os.system("cls")
    vipif = str(input("Are you vip player?: "))
    if vipif == "yes".lower():
        vip = True

    elif vipif == "no".lower():
        vip = False
        
    auraforequip = str(input("Which aura you want to have for auto equip?:"))
            

    print("Settings are saved, press Enter to get back to menu.")
            

def run():
    keyboard.wait("F1")
    try:
        while True:
                if vip == True:
                    Collection.everyvipspot()
                
                else:
                    Collection.everynonvipspot()
                    
    except NoRobloxWindowException:
        print("You must to open your roblox ")


def screenshot():
        os.system("ahk\\invetoryscreenopen.ahk")
        time.sleep(1)
        pyautogui.screenshot("invetoryscreen.png")
        time.sleep(1)
        os.system("ahk\\invetoryscreenclose.ahk")


def webhook(url, message):
    url = url
    message = message
    def send(themessage):
        data = {"content": message}
        response = requests.post(url, json=data)

    send(themessage=message)


def screenshot_send(url):
    file_path = "py/invetoryscreen.png"
    with open(file_path, "rb") as file:
        data = {"content": "**Item Inventory**",
                "image": {
                     "url": "attachment://inventoryscreen.png"
                }}
    
        response = requests.post(
            url,
            data=data,
            files={"file": ("inventoryscreen.png", file)}
        )
