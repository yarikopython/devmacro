import configparser
import logging
import time
import keyboard
import os

def autoequip():
        config = configparser.ConfigParser()
        config.read("py\\config.ini")
        aura = config.get("settings", "auratoequip")
        logging.info("Going to aura storage and search bar to search typed aura...")
        os.system("lib\\autoequip\\ahk\\autoequip.ahk")
        time.sleep(1)
        logging.info("Writing selected aura...")
        keyboard.write(aura)
        time.sleep(1)
        keyboard.press("Enter")
        time.sleep(1)
        logging.info("Quiting aura storage...")
        os.system("lib\\autoequip\\ahk\\autoequip2.ahk")