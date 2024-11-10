
import keyboard
import pyrobloxbot
import time
import pyautogui
import threading
import os
import sys
import logging

logging.basicConfig(filename="py\\macrolog.txt",
                    level=logging.INFO,
                    format="[%(asctime)s] - %(message)s",
                    datefmt="%H:%M:%S")



pressing = False




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
    logging("The screenshot was taken")
    time.sleep(1)
    logging.info("Closing quests...")
    os.system("ahk\\questscreenclose.ahk")
    logging.info("Completed.")



def questAHK():
  logging.info("Auto claiming every daily quest...")
  os.system("ahk\\questequip.ahk")
  logging.info("Finished auto claiming quests")



def autoequip(aura):
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
    


    

