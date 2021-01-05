import pyautogui

def msg_sender(i):

  
 pyautogui.click(x=398, y=964)
 pyautogui.typewrite('test %d' % i)
 pyautogui.press('enter')



for i in range(1000):
 msg_sender(i)
