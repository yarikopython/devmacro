from functions import settings, run
from pyrobloxbot import NoRobloxWindowException
import os
import threading
import pyautogui
import keyboard
import requests
import time

global vip
global pressing

pressing = False
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
                settings()
                os.system("cls")
            case 2:
                os.system("cls")
                print(webhok_text)
                os.system("cls")
                
            case 3:
                print(run_text)
                     
            case 4:

                print(exit_text)
                exit()
        
main()