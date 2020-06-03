import time
import pyautogui

(x,y)=pyautogui.position()

slotOne = "Box(left=637, top=988, width=27, height=13)"
slotTwo = "Box(left=717, top=988, width=27, height=13)"
slotThree = "Box(left=797, top=988, width=27, height=13)"
slotFour = "Box(left=877, top=988, width=27, height=13)"
slotFive = "Box(left=957, top=988, width=27, height=13)"
slotSix = "Box(left=1037, top=988, width=27, height=13)"
slotSeven = "Box(left=1117, top=988, width=27, height=13)"
slotEight = "Box(left=1197, top=988, width=27, height=13)"
slotNine = "Box(left=1277, top=988, width=27, height=13)"

def CurrentInvent():
    try:
        inventSlot =  [pyautogui.locateOnScreen('inventOne.png'), pyautogui.locateOnScreen('inventTwo.png'), pyautogui.locateOnScreen('inventThree.png'), pyautogui.locateOnScreen('inventFour.png'), pyautogui.locateOnScreen('inventFive.png'), pyautogui.locateOnScreen('inventSix.png'), pyautogui.locateOnScreen('inventSeven.png'), pyautogui.locateOnScreen('inventEight.png'), pyautogui.locateOnScreen('inventNine.png')]
        
    except:
        exit()

def findSword():
    try:  
        swordimage = pyautogui.locateOnScreen('ironSword.png')
        print("Sword One Found!")
        print(swordimage) 
        print("Finished attacking!")        
    except:
        print("No Sword Found!")
        exit()

def attack():
    pyautogui.click(x,y)
    time.sleep(0.2)
        
def eat():
    pyautogui.scroll(200)
    try:  
        foodimage = pyautogui.locateOnScreen('images/food/steak.png')
        print("Steak One Found!")
        print(foodimage)
        #TO DO - Find location of each inventory space!
        #TO DO - Keyboard press the number for the inventory slot!
        pyautogui.mouseDown(x,y, button="right")
        time.sleep(3.6)
        pyautogui.mouseUp(x,y, button="right") 
        print("Finished eating!")        
    except:
        print("No Food Found!")
        exit()


#Main Program
time.sleep(5)
while True:
    findSword()
    pyautogui.scroll(-200)
    for x in range(200):
        attack()   
    eat()

