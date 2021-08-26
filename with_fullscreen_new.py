import numpy as np
import cv2
from mss import mss
from PIL import Image
import scipy.misc
from matplotlib import cm
import pytesseract
from pytesseract import Output
import time
import pyautogui
import xlsxwriter
from time import strftime
import os
from datetime import datetime
import math
import sys
import keyboard


def read_screen(loc):
	sct = mss()
	sct_img = sct.grab(loc)
	return sct_img


count = 0


try :
	os.mkdir("Data")
except OSError:
	print("Folder Created")

path = "Data/"
waktu = strftime("%H:%M:%S")
tanggal = strftime("%d-%m-%Y")

workbook = xlsxwriter.Workbook(os.path.join(path , str(tanggal) + str(waktu)+'.xlsx'))
worksheet = workbook.add_worksheet()

worksheet.write(1, 2, 'Data')
worksheet.write(1, 3, 'Blower Hisap')

row = 2
col = 2
Value1 = 0
count = 0
iterate = 800
startX = 3
maxX = 1848
startY = 730

pyautogui.moveTo(startX, startY, duration=1)

time.sleep(2)

while 1:
	mon1 = {'top': 40, 'left': 135, 'width': 60, 'height': 35}
	mon2 = {'top': 275, 'left': 557, 'width': 50, 'height': 35}
	screen1 = read_screen(mon1)
	#screen2 = read_screen(mon2)

	image1 = np.array(screen1)
	resize_scaling = 200
	resize_width = int(image1.shape[1] * resize_scaling/100)
	resize_hieght = int(image1.shape[0] * resize_scaling/100)
	resized_dimentions = (resize_width, resize_hieght)
	image1 =  cv2.resize(image1, resized_dimentions, interpolation=cv2.INTER_AREA)
	gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	

	thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
							cv2.THRESH_BINARY, 17, 23)


	custom_config1 = r'--oem 3 --psm 6 outputbase digits'
	custom_config2 = r'-l eng --psm 6'
	Value1 = pytesseract.image_to_string(thres, config=custom_config1)
	

	count = count + 1

	ceilX = math.ceil(((maxX - startX)*count / iterate) + startX )
	pyautogui.moveTo(ceilX, startY, duration=0.2)
	cv2.imshow('test', np.array(thres))	
	time.sleep(0.1)
	cv2.destroyWindow('test')
	try:	
		val = float(Value1)
		print(Value1)
		#print(pyautogui.position())
		worksheet.write(row, 2, val)
		row = row + 1
	except :
		pass


	

	if (cv2.waitKey(1) & 0xFF) == ord('q'):
		workbook.close()
		cv2.destroyAllWindows()
		sys.exit()
		break


	if count == iterate : 
		workbook.close()
		cv2.destroyAllWindows()
		sys.exit()
		break

	