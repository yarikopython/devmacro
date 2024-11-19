import logging, os, time

def questAHK():
        logging.info("Auto claiming every daily quest...")
        os.system("lib\\autoquest\\ahk\\questequip.ahk")
        logging.info("Finished auto claiming quests")
        time.sleep(2)