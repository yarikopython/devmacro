import keyboard
from gui import detect

keyboard.add_hotkey("F1", lambda: detect())

keyboard.wait("F3")