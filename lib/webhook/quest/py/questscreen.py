import logging, os, time, pyautogui


def questscreen():
    logging.info("Opening quest to screenshot...")
    os.system("lib/webhook/quest/ahk/questscreenopen.ahk")
    time.sleep(1)
    logging.info("Taking screenshot of quests...")
    pyautogui.screenshot("lib/screenshots/questscreen.png")
    logging.info("The screenshot was taken")
    time.sleep(1)
    logging.info("Closing quests...")
    os.system("lib/webhook/quest/ahk/questscreenclose.ahk")
    logging.info("Completed.")