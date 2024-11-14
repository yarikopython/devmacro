from py.gui import webhok_text, run_text, about_text, about_project, exit_text, menu
from py.functions import settings, screenshots_send, storagescreen, inventoryscreen, questscreen, run
import pyrobloxbot

import os

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
                print(run_text)
                print("\n press F1 to run the macro, to stop press F3.")
                run()
                os.system("cls")
                
            case 3:
                print(exit_text)
                break
                     
            case 4:
                about_project()