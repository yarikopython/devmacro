import logging, os, time, pyautogui


def storagescreen():
     logging.info("Opening aura storage to screenshot...")
     os.system("lib/webhook/storage/ahk/storagescreenopen.ahk")
     time.sleep(1)
     logging.info("Taking Screenshot...")
     pyautogui.screenshot("lib/screenshots")
     logging.info("The screenshot was taken.")
     time.sleep(1)
     logging.info("Closing aura storage...")
     os.system("lib/webhook/storage/ahk/storagescreenclose.ahk")
     logging.info("Completed.")


