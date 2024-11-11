from py.automation import inventoryscreen, storagescreen, questscreen
from pyrobloxbot import NoRobloxWindowException
from webhook import webhook_url
from detect import start
import os
import requests
import keyboard
import logging

import pyautogui
import time
import threading

vip = False
running = False

logging.basicConfig(filename="py\\webhooklog.txt",
level=logging.INFO,
format="[%(asctime)s] - %(message)s",
datefmt="%H:%M:%S")


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
    logging.info("Getting png paths...")
    inventory_path = "py\\invetoryscreen.png"
    storage_path = "py\\storagescreen.png"
    quest_path = "py\\questscreen.png"
    log_path = "py\\macrolog.txt"
    logging.info("Completed.")


    logging.info("Checking if files are existing...")
    if not os.path.exists(inventory_path):
        logging.info("Making a screenshot from inventory...")
        inventoryscreen()
    if not os.path.exists(storage_path):
        logging.info("Making a screenshot from storage...")
        storagescreen()
    if not os.path.exists(quest_path):
        logging.info("Making a screenshot from quests...")
        questscreen()

    logging.info("Completed.")


    time.sleep(1)

    logging.info("Starting to open files...")

    with open(inventory_path, "rb") as inventory_file, \
        open(storage_path, "rb") as storage_file, \
        open(quest_path, "rb") as quest_file, \
        open(log_path, "rb") as log_file:
    
    logging.info("Completed.")

            
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

        logging.info("Sending files to users webhook...")

            inventory = requests.post(
                                url,
                                data=inventory_data,
                                files={"file": inventory_file}
                                )
            logging.info()

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

            logging.info("Finished with webhook send.")

            logging.info("Removing files to make fresh screenshots in the next time...")

            os.remove(inventory_path)
            os.remove(storage_path)
            os.remove(quest_path)
            os.remove(log_path)

            logging.info("Completed.")



def run():
    pass