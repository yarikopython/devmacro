from macro import Collection, screenshot, autoequip, autoquest, exiting
from functions import settings, webhook, run
import os
import threading
import pyautogui
import keyboard
import requests
import time

global vip

vip = False

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
                
                os.system("cls")
            case 2:
                os.system("cls")
                print(webhok_text)
                webhook()
                os.system("cls")
                
            case 3:
                print(run_text)
                while True:
                    run_thread = threading.Thread(target=run())
                    exit_thread = threading.Thread(target=exiting())
                    time.sleep(5)
                    run_thread.run()
                    exit_thread.run()                    

                
            case 4:

                print(exit_text)
                exit()
        
main()