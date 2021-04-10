# remember to download pyautogui moduel
# or it will not work

import random

# 製造行為方程式
# 製作第一個基因組
# 自交，生出一百個小孩
# 一百個小孩投入戰場上，開始競爭
# 每個小孩都會得到自己在競技場上的分數
# 留下最好的1隻，自交，繼續第二步驟
# 過了一百代，最後留下來的小孩就是我們要的基因，也就是我們的BOT

# 製作第一個基因組，全部都是一(自交後會有各種可能，機率為常態分佈)
# 輸入格式為int, 決定基因組之等為基因數量
def Make_First_Gene(alleleQuantity):
    answer = [1] * alleleQuantity
    return answer

# 將兩組2n基因組交配，回傳孩子的基因組
# 兩個輸入須為list格式，記得兩者長度必須相同，而且兩者都是由0, 1, 2構成
# 每一個數字都是基因組的等為基因，0為隱性(aa)，1為半顯性(Aa)，2為顯性(AA)
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

# 將一個2n的基因減數分裂，回傳一個配子的1n基因片段(被Fertilization使用)
# 輸入須為list格式，記得兩者長度必須相同，而且兩者都是由0, 1, 2構成
# 每一個數字都是基因組的等為基因，0為隱性(aa)，1為半顯性(Aa)，2為顯性(AA)
def Meiosis(listOfGene):
    answerGene = []
    processingGene = listOfGene
    length = len(processingGene)

    for i in processingGene:
        answerGene.append(Meiosis_Allele(i))

    return answerGene

# 將一組等位基因做減數分裂(被Meiosis使用)
# 輸入須為int格式，只能是是0, 1, 2其中一個
# 0為隱性(aa)，1為半顯性(Aa)，2為顯性(AA)
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


































