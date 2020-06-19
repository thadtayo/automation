'''
Script to autoclick Replay on Raid Shadow Legends every 10 seconds.
full screen: 1072 935
half screen: 1524 997
'''
import time, pyautogui, sys

if sys.argv[1] == 'h':
	x = 1524
	y = 997
elif sys.argv[1] == 'f':
	x = 1072
	y= 935

else:
	print('Input an argument: f or h.')
	exit()

while True:
	pyautogui.click(x, y)
	time.sleep(10)