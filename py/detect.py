from PIL import Image
import pytesseract
import pyautogui
import os
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'B:\devmacro\pytesseract\tesseract.exe'

biomes = [ "Hell", "Corruption", "Sandstorm", "Starfall", "Null"]

def detect():
    screenshot = pyautogui.screenshot("biom.png", (20, 945, 160, 30))
    cleaned = ""
    image_path = os.path.join("biom.png")
    save = screenshot.save(image_path)
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image=image)
    oldbiome = ""
    newbiome = ""
    if "Normal" in text:
        pass
    if "Rainy" in text:
        pass
    if "Windy" in text:
        pass
    if "Sandstorm" in text:
        pass
    
    return text

keyboard.add_hotkey("F1", lambda: print(detect()))
keyboard.wait("F3")