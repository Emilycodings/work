import pyautogui


#x,y = pyautogui.position()
#print('x={0}, y={1}' .format(x, y))

def todoadd(i):
	pyautogui.click(x=1729, y=128)
	#pyautogui.click(x=1729, y=128)


	pyautogui.moveTo(44,107,1)
	pyautogui.click(x=44, y=107)   
	pyautogui.typewrite('test %d' % i)  
    
    pyautogui.moveTo(103,293,1)
    pyautogui.click(x=103, y=293) 

    pyautogui.moveTo(72,375,1)
    pyautogui.click(x=72, y=375)	

    pyautogui.moveTo(397,184,1)
    pyautogui.click(x=397, y=184)	

	pyautogui.moveTo(927,613,1)
	pyautogui.click(x=927, y=613) 

    pyautogui.moveTo(297,533,1)
	pyautogui.click(x=297, y=533) 



for i in range(1):
	todoadd(i)

