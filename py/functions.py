from automation import inventoryscreen, storagescreen, questscreen, autoequip, questAHK
from pyrobloxbot import NoRobloxWindowException

import os
import requests
import keyboard
import logging

import pyautogui
import time
import threading
import sys
import configparser
from automation import config



if "settings" not in config.sections():
    config.add_section("settings")



vip = False
running = True


def settings():
        
    os.system("cls")
    vipif = input("Are you vip player?: ")
    if vipif == "yes".lower():
        vip = True
        config.set("settings", "vip", str(vip))

    else:
        vip = False
        config.set("settings","vip", str(vip))
        
    auraforequip = str(input("Which aura you want to have for auto equip?:"))
    userid = int(input("Please paste your user id to get ping: "))
    webhook_url = str(input("Please paste your webhook url: "))

    config.set("settings", "auratoequip", auraforequip)
    config.set("settings", "userid", userid)
    config.set("settings", "webhook_url", webhook_url)

    with open("py\\config.ini", "w") as configfile:
        config.write(configfile)

    print("Settings are saved, press Enter to get back to menu.")
            







def screenshots_send():
    logging.info("Getting png paths...")
    inventory_path = "py\\invetoryscreen.png"
    storage_path = "py\\storagescreen.png"
    quest_path = "py\\questscreen.png"
    config.read("py\\config.ini")
    webhook_url = config.get("settings", "webhook_url")

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
        open(quest_path, "rb") as quest_file:
    
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
                                url= webhook_url,
                                data=inventory_data,
                                files={"file": inventory_file}
                                )


            storage = requests.post(
                                url=webhook_url,    
                                data=storage_data,
                                files={"file": storage_file}
                                )
                            
            quest = requests.post(
                                url=webhook_url,
                                data=quest_data,
                                files={"file": quest_file}
                                )
            

            logging.info("Finished with webhook send.")

            logging.info("Removing files to make fresh screenshots in the next time...")

            inventory_file.close()
            storage_file.close()
            quest_file.close()

            os.remove(inventory_path)
            os.remove(storage_path)
            os.remove(quest_path)

            logging.info("Completed.")



def clearlogs(filepath):
    with open(file=filepath, mode="w") as file:
        file.write("")
        file.close()


def exit():
    while True:
        keyboard.wait('f3')
        os._exit(1)        

def run():
    clearlogs("py\\macrolog.txt")
    logging.info("Starting the program.")
    while True:
        threading.Thread(target=exit).start()
        questAHK()
        time.sleep(4)
        autoequip("Glock")
        time.sleep(4)
        screenshots_send()


"""time.sleep(2)
settings()
time.sleep(1)
screenshots_send()"""