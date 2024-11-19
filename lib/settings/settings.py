import logging, configparser, os

config = configparser.ConfigParser()


logging.basicConfig(filename="lib/settings/macrolog.txt",
                        level=logging.INFO,
                        format="[%(asctime)s] - %(message)s",
                        datefmt="%H:%M:%S")

    

def config_ini(): #creating config.ini
    with open("config.ini", "w") as filepath:
        config.write(filepath)
    

def clearlogs(filepath):
    with open(file=filepath, mode="w") as file:
        file.write("")
        file.close()



def settings():
    logging.info("Starting settings...")
    if not os.path.exists("lib/settings/config.ini"):
        config_ini()

    if "settings" not in config.sections():
        config.add_section("settings")

    os.system("cls")
    vipif = input("Are you vip player?: ")
    if vipif == "yes".lower():
        vip = True
        config.set("settings", "vip", str(vip))

    else:
        vip = False
        config.set("settings","vip", str(vip))
    
    logging.info("Started settings")
        
    auraforequip = str(input("Which aura you want to have for auto equip?:"))
    webhook_url = str(input("Please paste your webhook url: "))

    config.set("settings", "auratoequip", auraforequip)
    config.set("settings", "webhook_url", webhook_url)

    with open("lib/settings/config.ini", "w") as configfile:
        config.write(configfile)

    print("Settings are saved, press Enter to get back to menu.")
    logging.info("Ended settings")

