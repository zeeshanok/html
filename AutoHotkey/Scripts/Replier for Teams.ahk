#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#IfWinActive ahk_exe Teams.exe
+Insert::
Send ^c
Sleep, 300
phrase := Clipboard
Send, c
Send, >
Send, %phrase%{ShiftDown}{Enter}{Enter}{ShiftUp}
return

; ^CapsLock::
; Send, {Ctrl Shift M}
#IfWinActive