#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance, Force


Sleep, 2000

Send {Esc}
Sleep, 1000
Send {Esc}


MouseMove, 47, 600 ; Open quest
Sleep, 1000
MouseClick


MouseMove, 1202, 614 ; "Daily quest"
Sleep, 1000
MouseClick

MouseMove, 1201, 557 ; 1st quest
Sleep, 1000
MouseClick



MouseMove, 1202, 614 ; 2nd quest
Sleep, 1000
MouseClick



MouseMove, 1139, 609 ; 3rd quest
Sleep, 1000
MouseClick



MouseMove, 1412, 295 ; Closing quest
Sleep, 1000
MouseClick

