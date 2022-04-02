import os.path
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import time
import keyboard
import threading
import pystray
import config
from PIL import Image, ImageTk
from pystray import MenuItem as item
from pygame import mixer
from get_info import info
from hud import hud

#print(get_info.get_region())
#print(os.path.exists("config.ini"))
def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)
running = False
pr_str = None
pr_std = None
prt = 0
mixer.init()
mixer.music.load(resource_path('Air-raid-siren.mp3'))
#mixer.music.play()
if os.path.exists(config.get_path()) == False:
	hud.open_settings()
else:
	running = True
presed_key = ""
def key_pres():
	while True:
		global presed_key
		if keyboard.read_key() == "home":
			presed_key = "home"
		if keyboard.read_key() == "end":
			presed_key = "end"
		time.sleep(1)
threading1 = threading.Thread(target=key_pres)
threading1.daemon = True
threading1.start()
def icond():
	def pausem():
		mixer.music.stop()
	def quit_window():
		global running
		running = False
	def optionsb():
		hud.open_settings()
	image=Image.open(resource_path("favicon.ico"))
	menu = (item('Quit', quit_window), item('Pause', pausem), item('Options', optionsb))
	icon=pystray.Icon("name", image, "AirRade Reworked",menu)
	icon.run()
threading2 = threading.Thread(target=icond)
threading2.daemon = True
threading2.start()
while running == True:
	if prt <= time.time():
		prt = time.time() + 5
		if pr_str == None:
			if config.get('onlyregion') == 'True':
				pr_str = info.get_rgndst_info(config.get('region'), True)
			else:
				pr_str = info.get_rgndst_info(config.get('region'), True)
				pr_std = info.get_rgndst_info(config.get('district'), False)
		else:
			if config.get('onlyregion') == 'True':
				if pr_str != info.get_rgndst_info(config.get('region'), True):
					if info.get_rgndst_info(config.get('region'), True) == True:
						pr_str = True
						print('Alarm!!!!')
						mixer.music.play()
					else:
						pr_str = False
						print('Alarm is stopped')
						mixer.music.play()
			else:
				if pr_str != info.get_rgndst_info(config.get('region'), True) or pr_std != info.get_rgndst_info(config.get('district'), False):
					if info.get_rgndst_info(config.get('region'), True) != pr_str:
						if info.get_rgndst_info(config.get('region'), True) == True:
							pr_str = True
							print('Alarm!!!!')
							mixer.music.play()
						else:
							pr_str = False
							print('Alarm is stopped')
							mixer.music.play()
					else:
						if info.get_rgndst_info(config.get('district'), False) == True:
							pr_std = True
							print('Alarm!!!!')
							mixer.music.play()
						else:
							pr_std = False
							print('Alarm is stopped')
							mixer.music.play()
	time.sleep(0.5)
	if presed_key == "home":
		presed_key = " "
		running = False	
	if presed_key == "end":
		presed_key = " "
		mixer.music.stop()
