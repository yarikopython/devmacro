from macro import Collection
import os
import requests
import keyboard
from pyrobloxbot import NoRobloxWindowException

vip = False

def settings():
    global vip
    global auraforequip
    while True:
        
        os.system("cls")
        vipif = str(input("Are you vip player?: "))
        if vipif == "yes".lower():
            vip = True

        elif vipif == "no".lower():
            vip = False
        
        auraforequip = str(input("Which aura you want to have for auto equip?:"))
            

        print("Settings are saved, press Enter to get back to menu.")

def run():
    while True:
        try:
            if vip == True:
                Collection.everyvipspot()
        
            else:
                Collection.everynonvipspot()
            
        except NoRobloxWindowException:
            print("You must to open your roblox ")
            



def webhook(url, message):
    url = url
    message = message
    def send(themessage):
        data = {"content": message}
        response = requests.post(url, json=data)

    send(themessage=message)

