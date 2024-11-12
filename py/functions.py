from automation import inventoryscreen, storagescreen, questscreen, autoequip, questAHK
from pyrobloxbot import NoRobloxWindowException
from detect import start

import os
import requests
import keyboard
import logging

import pyautogui
import time
import threading
import sys

global vip
global auraforequip
global webhook_url

vip = False
running = True


def settings():
        
    os.system("cls")
    vipif = str(input("Are you vip player?: "))
    if vipif == "yes".lower():
        vip = True

    else:
        vip = False
        
    auraforequip = str(input("Which aura you want to have for auto equip?:"))
    webhook_url = str(input("Please paste your webhook url: "))
            

    print("Settings are saved, press Enter to get back to menu.")
            



webhook_url = "https://discord.com/api/webhooks/1302719341384700038/qp_pTHYEemyxMnusqOwdkvh4_9gU_quQ3NqFKX7-F8vqRbIoJTuSAQfThLpWAFaPhKiy"





def screenshots_send(url):
    logging.info("Getting png paths...")
    inventory_path = "py\\invetoryscreen.png"
    storage_path = "py\\storagescreen.png"
    quest_path = "py\\questscreen.png"
    log_path = "py\\macrolog.txt"
    logging.info("Completed.")


    logging.info("Checking if files are  not existing...")
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

            inventory_file.close()
            storage_file.close()
            quest_file.close()
            log_file.close()

            os.remove(inventory_path)
            os.remove(storage_path)
            os.remove(quest_path)

            logging.info("Completed.")


def onpress():
    global running
    while running:
        if os.path.exists("stop_flag.txt"):
            running = False
            break     

def run():
    global running

    threading.Thread(target=onpress, daemon=True).start()

    while True:
        questAHK()
        time.sleep(2)
        autoequip("Glock")
        time.sleep(2)
        screenshots_send(webhook_url)
    

<<<<<<< HEAD

=======
time.sleep(2)
run()
>>>>>>> 9901b0b9e7d71272e4eb20e40287cc479666c57a