import pyautogui as auto
import time
#import cv2
import threading
import _thread
#from PIL import *
#import matplotlib as mpl
#mpl.use('Agg')
#import matplotlib.pyplot as plt
#import numpy as np

class Bot(threading.Thread):
	adr = None
	opr = None
	def __init__(self, adr,opr):
		threading.Thread.__init__(self)
		self.opr = opr
		if(adr is not None):
			self.adr = adr
		else:
			print("")

	def run(self):
		if(self.opr == 'browser'):
			self.winOpen(self.adr)
		elif(self.opr == 'paint'):
			self.paintOpen()
		else:
			print("Unrecognizable operation")

	def winOpen(self, adr):
		auto.keyDown('winleft')
		auto.keyUp('winleft')
		time.sleep(2)
		auto.typewrite('chrome')
		time.sleep(2)
		auto.keyDown('enter')
		auto.keyUp('enter')
		time.sleep(2)
		auto.typewrite(str(adr))
		auto.keyDown('enter')
		auto.keyUp('enter')

	def paintOpen(self):
		auto.keyDown('winleft')
		auto.keyUp('winleft')
		time.sleep(2)
		auto.typewrite('paint')
		time.sleep(2)
		auto.keyDown('enter')
		auto.keyUp('enter')
		time.sleep(2)

		auto.keyDown('alt')
		auto.keyDown('space')
		auto.keyUp('alt')
		auto.keyUp('space')
		auto.keyDown('down')
		auto.keyUp('down')
		auto.keyDown('down')
		auto.keyUp('down')
		auto.keyDown('down')
		auto.keyUp('down')
		auto.keyDown('down')
		auto.keyUp('down')
		auto.keyDown('enter')
		auto.keyUp('enter')



		auto.moveTo(200, 300)

		x = 50
		y = 0
		err = 0
		x0 = 200
		y0 = 300

		while x >= y:
			auto.moveTo(x0 + x, y0 +y)
			auto.click(x0 + x, y0 +y)
			auto.moveTo(x0 + y, y0 +x)
			auto.click(x0 + y, y0 +x)
			auto.moveTo(x0 - y, y0 +x)
			auto.click(x0 - y, y0 +x)
			auto.moveTo(x0 - x, y0 +y)
			auto.click(x0 - x, y0 +y)
			auto.moveTo(x0 - x, y0 - y)
			auto.click(x0 - x, y0 - y)
			auto.moveTo(x0 - y, y0 - x)
			auto.click(x0 - y, y0 - x)
			auto.moveTo(x0 + y, y0 -x)
			auto.click(x0 + y, y0 -x)
			auto.moveTo(x0 + x, y0 -y)
			auto.click(x0 + x, y0 -y)

			if (err <= 0):
				y += 1
				err += 2*y +1

			if (err > 0):

				x -= 1;
				err -= 2*x +1;

#	def findImage(self, image):

#		try:
#			screenshot = ImageGrab.grab()
#			screenshot_numpy = np.array(screenshot.getdata(), dtype="uint8").reshape((screenshot.size[1], screenshot.size[0], 3))
#			screenshot_gray = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2GRAY)
#			template = cv2.imread(image, 0)
#			w, h = template.shape[::-1]

#			res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
#			threshold = 0.8

#			apu = np.where(res >= threshold)
#			loc = np.array(apu)[:,1]

#			loc[0] = loc[0]+(h/2)
#			loc[1] = loc[1]+(w/2)
#			return loc

#		except:
#			print("Template not found")
#			return None




