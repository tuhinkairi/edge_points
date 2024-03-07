import pyautogui
from wonderwords import RandomSentence
import time

'''
you just need to place the cursor over the edge browser !
'''

def get_position():
    time.sleep(5) 
    x, y = pyautogui.position()
    return {'x': x,'y': y} # return the position 

def get_views(loc):
    pos_x = loc['x']
    pos_y = loc['y']
    word = RandomSentence() # random words 
    round = input("enter how many time to simulate :-> ")
    for i in range(int(round)):
        print(word.sentence())
        pyautogui.moveTo(pos_x,pos_y,duration=.5)
        pyautogui.click()
        pyautogui.hotkey("ctrl","t")
        pyautogui.keyDown("/")
        pyautogui.keyDown("backspace")
        pyautogui.typewrite(word.sentence(),interval=.1)
        pyautogui.keyDown("enter")
        time.sleep(1)
        pyautogui.typewrite(['tab', 'space', 'space', 'tab', 'space', 'space', 'space'], interval=.3)
        time.sleep(2)
        pyautogui.hotkey("ctrl","W")
        time.sleep(1)
    
        
if __name__=="__main__":
    get_views(get_position())