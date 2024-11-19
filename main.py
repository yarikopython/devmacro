from lib.sublib.gui import (
    run_text,
    exit_text,
    macro_text,
    about_project,
    menu
)
from lib.autoquest.py.autoquest import questAHK
from lib.autoequip.py.autoequip import autoequip
from lib import sendscreenhot
from lib.settings.settings import settings
import threading
import time
import os
import keyboard
    

def run():
    thread = threading.Thread(target=exit)

    keyboard.wait("f1")
    while True:
        thread.start()
        questAHK()
        time.sleep(600)
        autoequip()

def run_macro():
    keyboard.wait("f1")
    global running_flag
    running_flag = True
    while running_flag:
        questAHK()
        time.sleep(600)  # Delay between actions
        autoequip()
        time.sleep(600)
        sendscreenhot()
        
    print("Macro stopped.")

def monitor_key():
    global running_flag
    while True:
        if keyboard.is_pressed("F3"):
            if running_flag:
                # Stop the Python script entirely when F3 is pressed
                print("Stopping macro via F3...")
                os._exit(0)  # Exit the script immediately
            break

def run():
    thread_monitor = threading.Thread(target=monitor_key)
    thread_macro = threading.Thread(target=run_macro)

    thread_monitor.start()
    thread_macro.start()

    # Wait for threads to finish
    thread_monitor.join()
    thread_macro.join()

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

main()