
import keyboard
import pyrobloxbot
import time
import pyautogui
import pydirectinput as dinput
import threading
import os
import sys

global pressing

pressing = False

# call function to click
def clickAHK():
  # calls terminal to run the ahk script with the ahk exe file, your path may be different
  os.system("ahk\\click.ahk")

def press_f():
    while pressing:
        keyboard.press_and_release("f")
        time.sleep(0.1)

def camera():
    os.system("ahk\\cameraalign.ahk")

def autoquest():
    while True:
        clickAHK()
        time.sleep(900)




def autoequip(aura):
    while True:
        equipaura = aura
        os.system("ahk\\autoequip.ahk")
        time.sleep(1)
        keyboard.write(equipaura)
        time.sleep(1)
        keyboard.press("Enter")
        time.sleep(1)
        os.system("ahk\\autoequip2.ahk")
        time.sleep(900)
    

def screenshot():
    while True:
        os.system("ahk\\invetoryscreenopen.ahk")
        pyautogui.screenshot("invetoryscreen.png")
        os.system("ahk\\invetoryscreenclose.ahk")
        time.sleep(900)
    

    

class Collection:

    @pyrobloxbot.require_focus
    def nonvipspot12():
        try:
            global pressing
            pressing = True
            f_thread = threading.Thread(target=press_f)
            f_thread.start()
            pyrobloxbot.reset_player()
            pyrobloxbot.walk_forward(1.0)

            pyrobloxbot.walk_left(4.0)
            pyrobloxbot.walk_back(4.7)

            pyrobloxbot.reset_player()

            pressing = False
        except pyrobloxbot.exceptions.NoRobloxWindowException:
            pressing = False
            print("\n You forgot to open Roblox!!!")
                

    @pyrobloxbot.require_focus
    def nonvipspot34():
        try:
            global pressing
            pressing = True
            f_thread = threading.Thread(target=press_f)
            f_thread.start()
            pyrobloxbot.reset_player()

            pyrobloxbot.jump()
            pyrobloxbot.walk_back(0.4)
            
            pyrobloxbot.jump()
            pyrobloxbot.walk_back(0.7)

            time.sleep(1)

            pyrobloxbot.walk_right(0.5)
            pyrobloxbot.jump()
            pyrobloxbot.walk_right(0.5)

            pyrobloxbot.jump()
            pyrobloxbot.walk_right(0.5)

            pyrobloxbot.walk_back(0.6)
            pyrobloxbot.jump()

            pyrobloxbot.walk_back(0.5)
            time.sleep(1)
            pyrobloxbot.walk_left(0.6)

            pyrobloxbot.walk_back(1.5)
            pyrobloxbot.walk_right(1)

            pyrobloxbot.reset_player()

            pressing = False
        except pyrobloxbot.exceptions.NoRobloxWindowException:
            pressing = False
            print("\n You forgot to open Roblox!!!")

    @pyrobloxbot.require_focus
    def nonvipspot56():
        try:
            global pressing
            pressing = True
            f_thread = threading.Thread(target=press_f)
            f_thread.start()
            pyrobloxbot.reset_player()
            pyrobloxbot.walk_forward(2.7)

            time.sleep(1)
            pyrobloxbot.walk_right(4)

            pyrobloxbot.jump()
            pyrobloxbot.walk_right(0.2)

            pyrobloxbot.walk_forward(7)
            pyrobloxbot.walk_left(0.9)

            pyrobloxbot.jump()
            pyrobloxbot.walk_left(0.3)

            pyrobloxbot.jump()
            pyrobloxbot.walk_left(0.3)
            pyrobloxbot.jump()

            pyrobloxbot.walk_left(0.5)
            time.sleep(1)
            
            pyrobloxbot.walk_forward(0.3)
            pyrobloxbot.jump()

            pyrobloxbot.walk_forward(0.2)
            pyrobloxbot.jump()

            pyrobloxbot.walk_forward(0.3)
            pyrobloxbot.jump()

            pyrobloxbot.walk_forward(0.2)
            pyrobloxbot.jump()

            pyrobloxbot.walk_forward(0.2)
            pyrobloxbot.walk_forward(0.3)

            pyrobloxbot.walk_left(0.2)
            pyrobloxbot.jump()

            pyrobloxbot.walk_left(0.1)
            pyrobloxbot.walk_back(0.3)

            pyrobloxbot.walk_left(0.4)
            pyrobloxbot.reset_player()

            pressing = False
        except pyrobloxbot.exceptions.NoRobloxWindowException:
            pressing = False
            print("\n You forgot to open Roblox!!!")

    def press_f():

        while pressing:
            keyboard.press_and_release("f")
            time.sleep(0.1)

    @pyrobloxbot.require_focus
    def spot12():
        try:
            global pressing
            pressing = True
            f_thread = threading.Thread(target=press_f)

            f_thread.start()
            pyrobloxbot.reset_player()

            time.sleep(1)
            pyrobloxbot.walk_forward(0.5)

            time.sleep(1)
            pyrobloxbot.walk_left(3.2)

            time.sleep(0.5)
            pyrobloxbot.walk_back(3.4)
            
            pyrobloxbot.reset_player()

            pressing = False
        except pyrobloxbot.exceptions.NoRobloxWindowException:
            pressing = False
            print("\n You forgot to open Roblox!!!")

    def spot34():
        global pressing
        pressing = True
        f_thread = threading.Thread(target=press_f)
        f_thread.start()
        pyrobloxbot.reset_player()
        time.sleep(1)
        pyrobloxbot.walk_back(0.37)
        pyrobloxbot.jump()
        pyrobloxbot.walk_back(0.5)
        time.sleep(1)
        pyrobloxbot.walk_right(0.39)
        time.sleep(1)
        pyrobloxbot.jump()
        pyrobloxbot.walk_right(0.45)
        pyrobloxbot.jump()
        pyrobloxbot.walk_right(0.5)
        pyrobloxbot.walk_back(0.4)
        pyrobloxbot.jump()
        pyrobloxbot.walk_back(0.5)
        time.sleep(1)
        pyrobloxbot.walk_left(0.8)
        time.sleep(1)
        pyrobloxbot.walk_back(1.0)
        pyrobloxbot.walk_right(0.5)
        pyrobloxbot.reset_player()

        pressing = False        
    
    def spot56():
        global pressing
        pressing = True
        f_thread = threading.Thread(target=press_f)
        f_thread.start()

        pyrobloxbot.reset_player()
        time.sleep(1)
        pyrobloxbot.walk_forward(2.3)
        time.sleep(1)
        pyrobloxbot.walk_right(3.2)
        pyrobloxbot.jump()
        pyrobloxbot.walk_right(0.2)
        time.sleep(1)
        pyrobloxbot.walk_forward(5.5)
        pyrobloxbot.walk_forward(0.5)
        pyrobloxbot.walk_left(0.5)
        pyrobloxbot.walk_forward(0.2)
        pyrobloxbot.jump()
        pyrobloxbot.walk_forward(0.2)
        pyrobloxbot.jump()
        pyrobloxbot.walk_forward(0.2)
        pyrobloxbot.walk_left(0.3)
        pyrobloxbot.jump()
        pyrobloxbot.walk_left(0.3)
        pyrobloxbot.jump()
        pyrobloxbot.walk_forward(0.2)
        pyrobloxbot.walk_left(0.2)
        pyrobloxbot.jump()
        pyrobloxbot.walk_left(0.2)
        pyrobloxbot.jump()
        pyrobloxbot.walk_left(0.37)
        pyrobloxbot.jump()
        pyrobloxbot.walk_left(0.2)
        pyrobloxbot.walk_back(0.3)
        pyrobloxbot.walk_left(2.8)
        pyrobloxbot.reset_player()


        pressing = False

    def everyvipspot():
        if keyboard.is_pressed("F3"):
            print("F3 pressed, exiting program.")
            sys.exit()
        
        Collection.spot12()

        if keyboard.is_pressed("F3"):
            print("F3 pressed, exiting program.")
            sys.exit()

        Collection.spot34()

        if keyboard.is_pressed("F3"):
            print("F3 pressed, exiting program.")
            sys.exit()
        Collection.spot56()

    def everynonvipspot():
        if keyboard.is_pressed("F3"):
            print("F3 pressed, exiting program.")
            sys.exit()
        Collection.nonvipspot12()

        if keyboard.is_pressed("F3"):
            print("F3 pressed, exiting program.")
            sys.exit()
        Collection.nonvipspot34()
        if keyboard.is_pressed("F3"):
            print("F3 pressed, exiting program.")
            sys.exit()
            
        Collection.nonvipspot56()


