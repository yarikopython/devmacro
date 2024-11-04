from py.macro import Collection, screenshot, autoequip, autoquest
import os
import pyautogui
import keyboard
import requests
import time



macro_text = """
##   ##    ##      ## ##   ### ##    ## ##   
 ## ##      ##    ##   ##   ##  ##  ##   ##  
# ### #   ## ##   ##        ##  ##  ##   ##  
## # ##   ##  ##  ##        ## ##   ##   ##  
##   ##   ## ###  ##        ## ##   ##   ##  
##   ##   ##  ##  ##   ##   ##  ##  ##   ##  
##   ##  ###  ##   ## ##   #### ##   ## ##   
                                             
"""

settings_text = """
 ## ##   ### ###  #### ##  #### ##    ####   ###  ##   ## ##    ## ##   
##   ##   ##  ##  # ## ##  # ## ##     ##      ## ##  ##   ##  ##   ##  
####      ##        ##       ##        ##     # ## #  ##       ####     
 #####    ## ##     ##       ##        ##     ## ##   ##  ###   #####   
    ###   ##        ##       ##        ##     ##  ##  ##   ##      ###  
##   ##   ##  ##    ##       ##        ##     ##  ##  ##   ##  ##   ##  
 ## ##   ### ###   ####     ####      ####   ###  ##   ## ##    ## ##   
                                                                       """

run_text = """
### ##   ##  ###  ###  ##  
 ##  ##  ##   ##    ## ##  
 ##  ##  ##   ##   # ## #  
 ## ##   ##   ##   ## ##   
 ## ##   ##   ##   ##  ##  
 ##  ##  ##   ##   ##  ##  
#### ##   ## ##   ###  ##  
                           
"""

webhok_text = """
##   ##  ### ###  ### ##   ###  ##   ## ##    ## ##   ##  ###  
##   ##   ##  ##   ##  ##   ##  ##  ##   ##  ##   ##  ##  ##   
##   ##   ##       ##  ##   ##  ##  ##   ##  ##   ##  ## ##    
## # ##   ## ##    ## ##    ## ###  ##   ##  ##   ##  ## ##    
# ### #   ##       ##  ##   ##  ##  ##   ##  ##   ##  ## ###   
 ## ##    ##  ##   ##  ##   ##  ##  ##   ##  ##   ##  ##  ##   
##   ##  ### ###  ### ##   ###  ##   ## ##    ## ##   ##  ### """

exit_text = """
### ###  ##  ##     ####   #### ##  
 ##  ##  ### ##      ##    # ## ##  
 ##       ###        ##      ##     
 ## ##     ###       ##      ##     
 ##         ###      ##      ##     
 ##  ##  ##  ###     ##      ##     
### ###  ##   ##    ####    ####    """





def settings():
    global vip
    os.system("cls")
    print(settings_text)
    vipif = input("Are you vip player?: ")
    if vipif == "yes".lower():
        vip = True

    elif vipif == "no".lower():
        vip = False
    
    print("Settings are saved, press Enter to get back to menu.")

def run():
    if vip == True:
        Collection.everyvipspot()
    
    else:
        Collection.everynonvipspot()
        

def webhook(url, message):
    url = url
    message = message
    def send(themessage):
        data = {"content": message}
        response = requests.post(url, json=data)

    send(themessage=message)



def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(macro_text)
    print("=" * 40)
    print("         Devmacro by darkness, v0.1      ")
    print("=" * 40)
    print("\n [1] - Settings")
    print("\n [2] - Discord Webhook")
    print("\n [3] - Run")
    print("\n [4] - Exit")

def main():
    while True:
        menu()
        choose = input("\nChoose one option: ")
        choice = int(choose)
        match choice:
            case 1:
                os.system("cls")
                settings()
                
            case 2:
                webhook()
                
            case 3:
                time.sleep(3)
                run()
            case 4:
                print(exit_text)
                exit()
        
