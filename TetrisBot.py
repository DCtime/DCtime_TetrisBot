# remember to download pyautogui moduel
# or it will not work

import random

def Meiosis(gene):
    
    randomNum = random.random()
    print(randomNum)
    
    if (gene == 0):
        return 0
    elif (gene == 1):
        if (randomNum < 0.5):
            return 0
        else:
            return 1
    elif (gene == 2):
        return 1
    else:
        print("Error, gene must be 0, 1 or 2")
    

print(Meiosis(3))
