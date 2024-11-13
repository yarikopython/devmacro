
import keyboard
import time
import pyautogui
import os
import logging
import configparser

logging.basicConfig(filename="py\\macrolog.txt",
                    level=logging.INFO,
                    format="[%(asctime)s] - %(message)s",
                    datefmt="%H:%M:%S")

config = configparser.ConfigParser()





def inventoryscreen():
        logging.info("Opening inventory to screenshot...")
        os.system("ahk\\invetoryscreenopen.ahk")
        time.sleep(1)
        logging.info("Taking screenshot")
        pyautogui.screenshot("py\\invetoryscreen.png")
        logging.info("Screnshot was taken")
        time.sleep(1)
        logging.info("Closing inventory...")
        os.system("ahk\\invetoryscreenclose.ahk")
        logging.info("Completed.")


def storagescreen():
     logging.info("Opening aura storage to screenshot...")
     os.system("ahk\\storagescreenopen.ahk")
     time.sleep(1)
     logging.info("Taking Screenshot...")
     pyautogui.screenshot("py\\storagescreen.png")
     logging.info("The screenshot was taken.")
     time.sleep(1)
     logging.info("Closing aura storage...")
     os.system("ahk\\storagescreenclose.ahk")
     logging.info("Completed.")


def questscreen():
    logging.info("Opening quest to screenshot...")
    os.system("ahk\\questscreenopen.ahk")
    time.sleep(1)
    logging.info("Taking screenshot of quests...")
    pyautogui.screenshot("py\\questscreen.png")
    logging.info("The screenshot was taken")
    time.sleep(1)
    logging.info("Closing quests...")
    os.system("ahk\\questscreenclose.ahk")
    logging.info("Completed.")



def questAHK():
        logging.info("Auto claiming every daily quest...")
        os.system("ahk\\questequip.ahk")
        logging.info("Finished auto claiming quests")
        time.sleep(2)



def autoequip():
        config = configparser.ConfigParser()
        config.read("py\\config.ini")
        aura = config.get("settings", "auratoequip")
        logging.info("Going to aura storage and search bar to search typed aura...")
        os.system("ahk\\autoequip.ahk")
        time.sleep(1)
        logging.info("Writing selected aura...")
        keyboard.write(aura)
        time.sleep(1)
        keyboard.press("Enter")
        time.sleep(1)
        logging.info("Quiting aura storage...")
        os.system("ahk\\autoequip2.ahk")
