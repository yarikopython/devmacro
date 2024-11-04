#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance, Force

MouseGetPos, vX,vY
; moves the mouse optional but just sort of a confirm that it's in the right spot
Send {Esc}
Sleep, 1000
Send {Esc}


MouseMove, 35, 620 ; Open quest
Sleep, 1000
MouseClick


MouseMove, 1212, 300 ; "Daily quest"
Sleep, 1000
MouseClick

MouseMove, 1317, 551 ; 1st quest
Sleep, 1000
MouseClick



MouseMove, 1320, 636 ; 2nd quest
Sleep, 1000
MouseClick



MouseMove, 1326, 720 ; 3rd quest
Sleep, 1000
MouseClick



MouseMove, 1392, 250 ; Closing quest
Sleep, 1000
MouseClick

