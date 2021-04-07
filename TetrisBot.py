# remember to download pyautogui moduel
# or it will not work

import pyautogui

def CombineGamete(int firstProbability. int secondProbability):
    finalResult = -1
    realFirstProbability = -1
    realSecondProbability = -1

    switch(firstProbability):
        case 0:
            realFirstProbability = 0
            break
        case 1:
            realFirstProbability = 0.5
            break
        case 2:
            realFirstProbability = 1
            break
    
    # 如果是X, 為aa X aa (0 X 0)
    # 如果是X, 為aa X Aa, Aa X aa (0 X 1 or 1 X 0)
    # 如果是X, 為AA X aa, aa X AA (2 X 0 or 0 X 2)
    # 如果是X, 為Aa X Aa (1 X 1)
    # 如果是X, 為AA X AA (2 X 2)
    
    return 0
    return 1
    return 2
