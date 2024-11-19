import logging, os, time, pyautogui


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