# remember to download pyautogui moduel
# or it will not work

import random

# 將兩組2n基因交配，回傳孩子的基因
def Fertilization(firstListOfGene, secondListOfGene):
    answerGene = []
    
    if (len(firstListOfGene) != len(secondListOfGene)):
        print("Two lists of genes must be the same length")
        return null

    firstProcessingGene = firstListOfGene
    secondProcessingGene = secondListOfGene

    firstProcessingGene = Meiosis(firstProcessingGene)
    secondProcessingGene = Meiosis(secondProcessingGene)
    
    for i in range(len(firstProcessingGene)):
        answerGene.append(firstProcessingGene[i] + secondProcessingGene[i])

    return answerGene

# 將一個2n的基因減數分裂，回傳一個配子的1n基因片段
def Meiosis(listOfGene):
    answerGene = []
    processingGene = listOfGene
    length = len(processingGene)

    for i in processingGene:
        answerGene.append(Meiosis_Allele(i))

    return answerGene

# 將一組等位基因做減數分裂(被Meiosis使用)
def Meiosis_Allele(gene):
    
    randomNum = random.random()
    #print(randomNum)
    
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
    
