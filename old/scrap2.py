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


def read_screen(loc):
	sct = mss()
	sct_img = sct.grab(loc)
	return sct_img


count = 0


try :
	os.mkdir("Data")
except OSError:
	print("Folder Created")



while 1:
	mon1 = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
	mon2 = {'top': 680, 'left': 400, 'width': 800, 'height': 50}
	screen1 = read_screen(mon1)
	#screen2 = read_screen(mon2)
	cv2.imshow('test', np.array(screen1))	


	if (cv2.waitKey(1) & 0xFF) == ord('q'):
		cv2.destroyAllWindows()
		break

