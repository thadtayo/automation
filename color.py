from PIL import Image, ImageGrab
import sys, time

if len(sys.argv) < 2:
	print('not enough args.')
	exit()

print('Get ready for screenshot! 3 seconds.')
time.sleep(3)

im = ImageGrab.grab()
color = im.getpixel((int(sys.argv[1]), int(sys.argv[2])))
print(color)

