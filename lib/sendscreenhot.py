import logging, time, os, configparser, requests, sys
from inventory.py.inventoryscreen import inventoryscreen
from quest.py.questscreen import questscreen
from storage.py.storagescreen import storagescreen

config = configparser.ConfigParser()

def screenshots_send():
    logging.info("Getting png paths...")
    inventory_path = "lib/screenshots/invetoryscreen.png"
    storage_path = "lib/screenshots/storagescreen.png"
    quest_path = "lib/screenshots/questscreen.png"
    config.read("lib/settings/config.ini")
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
            os.remove(quest_path) #removing to get fresh screenshots in the next time

            logging.info("Completed.")