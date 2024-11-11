from py.automation import inventoryscreen, storagescreen, questscreen
from pyrobloxbot import NoRobloxWindowException
from webhook import webhook_url
from detect import start
import os
import requests
import keyboard

import pyautogui
import time
import threading

vip = False
running = False


def settings():
    global vip
    global auraforequip
        
    os.system("cls")
    vipif = str(input("Are you vip player?: "))
    if vipif == "yes".lower():
        vip = True

    else:
        vip = False
        
    auraforequip = str(input("Which aura you want to have for auto equip?:"))
            

    print("Settings are saved, press Enter to get back to menu.")
            










def screenshots_send(url):
    inventory_path = "py\\invetoryscreen.png"
    storage_path = "py\\storagescreen.png"
    quest_path = "py\\questscreen.png"
    log_path = "py\\macrolog.txt"



    if not os.path.exists(inventory_path):
        inventoryscreen()
    if not os.path.exists(storage_path):
        storagescreen()
    if not os.path.exists(quest_path):
        questscreen()

    


    time.sleep(1)

    with open(inventory_path, "rb") as inventory_file, \
        open(storage_path, "rb") as storage_file, \
        open(quest_path, "rb") as quest_file, \
        open(log_path, "rb") as log_file:

            
            inventory_data = {"content": "**Item Inventory**",
                                "image": {
                                    "url": "attachment://inventoryscreen.png"
                                }}

            storage_data = {"content": "**Aura Storage**",
                                "image": {
                                        "url":"attachment://storagescreen.png"
                                }}

            quest_data = {"content": "**Daily Quest**",
                                        "image": {
                                            "url": "attachment://questscreen.png"
                                        }}

            log_data = {"content": "**Macro Logs**", }


            inventory = requests.post(
                                url,
                                data=inventory_data,
                                files={"file": inventory_file}
                                )

            storage = requests.post(
                                url=url,    
                                data=storage_data,
                                files={"file": storage_file}
                                )
                            
            quest = requests.post(
                                url=url,
                                data=quest_data,
                                files={"file": quest_file}
                                )
            
            logs = requests.post(url=url,
                                data=log_data,
                                files={"file": (log_path, log_file)})

            os.remove(inventory_path)
            os.remove(storage_path)
            os.remove(quest_path)



def run():
    pass