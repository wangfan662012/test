import os
import sys
from importlib import reload
import pythoncom
import pyHook
import time
import pywin32_system32
import win32
import requests

def onKeyboardEvent(event):
	if event.Key == 'F12':
		print(event.Key)
	#return True



def main():
	hm = pyHook.HookManager()
	hm.KeyDown = onKeyboardEvent
	hm.HookKeyboard()
	pythoncom.PumpMessages(1000)
	#hm.UnhookKeyboard()

if __name__ == '__main__':
	main()
