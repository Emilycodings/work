import pyautogui


#x,y = pyautogui.position()
#print('x={0}, y={1}' .format(x, y))

def todoadd(i):
	pyautogui.click(x=1729, y=128)
	#pyautogui.click(x=1729, y=128)


	pyautogui.moveTo(44,107,1)
	pyautogui.click(x=44, y=107)
	pyautogui.typewrite('test %d' % i)

	pyautogui.moveTo(308,531,1)
	pyautogui.click(x=308, y=531)


for i in range(10):
	todoadd(i)
