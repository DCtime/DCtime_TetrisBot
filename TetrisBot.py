import random
import time
from multiprocessing import Process, Pool
import os
import multiprocessing


# 製造行為方程式
# 製作第一個基因組
# 自交，生出一百個小孩
# 一百個小孩投入戰場上，開始競爭
# 每個小孩都會得到自己在競技場上的分數
# 留下最好的1隻，自交，繼續第二步驟
# 過了一百代，最後留下來的小孩就是我們要的基因，也就是我們的BOT

# ------------------------關於基因的函數-----------------------------------
# 製作第一個基因組，全部都是一(自交後會有各種可能，機率為常態分佈)
# 輸入格式為int, 決定基因組之等為基因數量
def Make_First_Genes(alleleQuantity, geneGroupQuantity, babyQuantity):
    if geneGroupQuantity == 1 or geneGroupQuantity == 2:
        return [[[[1] * alleleQuantity] * geneGroupQuantity] * babyQuantity]
    else:
        answer = []
        poleGeneQuantity = geneGroupQuantity // 3
        for _ in range(poleGeneQuantity):
            answer.append([[0] * alleleQuantity] * geneGroupQuantity)
            answer.append([[2] * alleleQuantity] * geneGroupQuantity)
        for _ in range(babyQuantity - poleGeneQuantity * 2):
            answer.append([[1] * alleleQuantity] * geneGroupQuantity)
        return answer

# 將兩組2n基因組交配，回傳孩子的基因組
# 兩個輸入須為list格式，記得兩者長度必須相同，而且兩者都是由0, 1, 2構成
# 每一個數字都是基因組的等為基因，0為隱性(aa)，1為半顯性(Aa)，2為顯性(AA)
def Fertilization(firstListOfGene, secondListOfGene):
    answerGene = []  # 儲存回傳的答案基因

    if (len(firstListOfGene) != len(secondListOfGene)):  # 當兩個基因長度不同的時候
        print("Two lists of genes must be the same length")  # 印出警語
        return null  # 結束程式

    firstProcessingGene = firstListOfGene  # 將輸入的值個別存入frirstProcessOfGene 和 SecondProcessOfGene
    secondProcessingGene = secondListOfGene

    firstProcessingGene = Meiosis(firstProcessingGene)  # 減數分裂
    secondProcessingGene = Meiosis(secondProcessingGene)

    for i in range(len(firstProcessingGene)):
        answerGene.append(firstProcessingGene[i] + secondProcessingGene[i])  # 受精

    return answerGene


# 將一個2n的基因減數分裂，回傳一個配子的1n基因片段(被Fertilization使用)
# 輸入須為list格式，記得兩者長度必須相同，而且兩者都是由0, 1, 2構成
# 每一個數字都是基因組的等為基因，0為隱性(aa)，1為半顯性(Aa)，2為顯性(AA)
def Meiosis(listOfGene):
    answerGene = []  # 儲存答案
    processingGene = listOfGene  # 將樹入的基因存入processingGene
    length = len(processingGene)  # 存基因的長度

    for i in processingGene:
        answerGene.append(Meiosis_Allele(i))  # 每一組等位基因做減數分裂

    return answerGene


# 將一組等位基因做減數分裂(被Meiosis使用)
# 輸入須為int格式，只能是是0, 1, 2其中一個
# 0為隱性(aa)，1為半顯性(Aa)，2為顯性(AA)
def Meiosis_Allele(gene):
    randomNum = random.random()  # 得到一個0~1的數字，存入randomNum
    # print(randomNum)

    if gene == 0:  # 如果等位基因為隱性
        return 0  # 減數分裂後必為隱性
    elif gene == 1:  # 如果等位基因為半顯性
        if (randomNum < 0.5):  # 小於0.5為隱性
            return 0
        else:
            return 1  # 大於等於0.5為顯性
    elif gene == 2:  # 如果等位基因為顯性
        return 1
    else:
        print("Error, gene must be 0, 1 or 2")  # 如果格式不符，回傳錯誤訊息


# 下一步製作俄羅斯方塊模擬器
# --------------------關於俄羅斯方塊的函數----------------------------

# 放置俄羅斯方塊函數(被TetrisMovement使用)
# 輸入俄羅斯方塊類型，俄羅斯方塊方向，俄羅斯方塊位置
# 回傳放置位置之最大高度，並完成設定板上的放置
# 俄羅斯方塊類型分七型，以字串表示：L, J, S, Z, T, O, I
# (代號意思請看我做的Google簡報)
# 俄羅斯方塊的方向:用0, 90, 180, 270表示(單位是度)
# 俄羅斯方塊的位置以離左側版框的距離來表示
# 如果是黏在最左邊，位置為0

def Place_TetrisBlock(type, rotation, location, board):
    # 設定檢查方塊初始位置
    # checkBlock[a][b], a為第a個方塊(最大3，從0開始數,順序為由左而右,第0列做完換第1列), b是0則是由上往下數位置, b是1則是由左向右數的位置
    checkBlock = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    # 儲存放置方塊之最大高度
    height = 0
    if type == "L":
        if rotation == 0:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [0, location + 2]
            checkBlock[3] = [1, location + 0]
        elif rotation == 90:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [2, location + 1]
        elif rotation == 180:
            checkBlock[0] = [0, location + 2]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [1, location + 2]
        elif rotation == 270:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [2, location + 0]
            checkBlock[3] = [2, location + 1]
        else:
            print("rotation not found. Available rotation are 0, 90, 180, and 270")
    elif type == "J":
        if rotation == 0:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [0, location + 2]
            checkBlock[3] = [1, location + 2]
        elif rotation == 90:
            checkBlock[0] = [0, location + 1]
            checkBlock[1] = [1, location + 1]
            checkBlock[2] = [2, location + 0]
            checkBlock[3] = [2, location + 1]
        elif rotation == 180:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [1, location + 2]
        elif rotation == 270:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [1, location + 0]
            checkBlock[3] = [2, location + 0]
        else:
            print("rotation not found. Available rotation are 0, 90, 180, and 270")
    elif type == "S":
        if rotation == 0 or rotation == 180:
            checkBlock[0] = [0, location + 1]
            checkBlock[1] = [0, location + 2]
            checkBlock[2] = [1, location + 0]
            checkBlock[3] = [1, location + 1]
        elif rotation == 90 or rotation == 270:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [2, location + 1]
        else:
            print("rotation not found. Available rotation are 0, 90, 180, and 270")
    elif type == "Z":
        if rotation == 0 or rotation == 180:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [1, location + 2]
        elif rotation == 90 or rotation == 270:
            checkBlock[0] = [0, location + 1]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [2, location + 0]
        else:
            print("rotation not found. Available rotation are 0, 90, 180, and 270")
    elif type == "T":
        if rotation == 0:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [0, location + 2]
            checkBlock[3] = [1, location + 1]
        elif rotation == 90:
            checkBlock[0] = [0, location + 1]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [2, location + 1]
        elif rotation == 180:
            checkBlock[0] = [0, location + 1]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [1, location + 2]
        elif rotation == 270:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [1, location + 1]
            checkBlock[3] = [2, location + 0]
        else:
            print("rotation not found. Available rotation are 0, 90, 180, and 270")
    elif type == "I":
        if rotation == 0 or rotation == 180:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [0, location + 1]
            checkBlock[2] = [0, location + 2]
            checkBlock[3] = [0, location + 3]
        elif rotation == 90 or rotation == 270:
            checkBlock[0] = [0, location + 0]
            checkBlock[1] = [1, location + 0]
            checkBlock[2] = [2, location + 0]
            checkBlock[3] = [3, location + 0]
        else:
            print("rotation not found. Available rotation are 0, 90, 180, and 270")
    elif type == "O":
        checkBlock[0] = [0, location + 0]
        checkBlock[1] = [0, location + 1]
        checkBlock[2] = [1, location + 0]
        checkBlock[3] = [1, location + 1]
    else:
        print("Type not found. Available type: L, J, S, Z, T, I, O ")

    stop = False  # 找停下來的位置
    while 1:  # 檢查每一個方塊
        for i in checkBlock:
            if i[0] + 1 > 17:  # 如果以碰到地板，stop = true
                # print("STOP")
                stop = True
                break
            elif board[i[0] + 1][i[1]] == "*":  # 每一個方塊下面是不是有東西，如果有，stop = true
                # print("STOP")
                stop = True
                break
        if stop == False:  # 如果stop == false，全部方塊下去一階
            for i in checkBlock:
                i[0] = i[0] + 1
        else:  # 如果stop == true，將"-"換成"*"(board)，並跳出迴圈
            for i in checkBlock:
                board[i[0]][i[1]] = "*"
                # print("i[0]", i[0])
                if 18 - i[0] > height:  # y方向越低越高
                    height = 18 - i[0]
                # print("height :", height)
            break
    return (height)


# 檢查版面函數(消行與計分)(被TetrisMovement使用)
# 會回傳此檢查所獲得的分數，並完成設定板上的消除
def CheckBoard(board):
    cleaned = []  # 紀錄消掉的行的編號

    for i in range(18):  # 在每一行中
        for j in range(10):
            if board[i][j] == "-":  # 如果有一個空的，不理
                break
        else:  # 如果都是"*",清掉那一行並標記起來
            board[i] = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
            cleaned.append(i)
    # print(cleaned)

    # 算分數
    # 一次一行 40分
    # 一次兩行 100分
    # 一次三行 300分
    # 一次四行 1200分
    # print(len(cleaned))
    score = 0

    if len(cleaned) == 1:
        score = 40
    elif len(cleaned) == 2:
        score = 100
    elif len(cleaned) == 3:
        score = 300
    elif len(cleaned) == 4:
        score = 1200

    # 將空著的行補起來
    # 從最小的編號開始補

    # print(cleaned)

    for level in cleaned:
        # print("level:", level)
        for i in range(level):
            # print("level - i:",level - i)
            for j in range(10):
                board[level - i][j] = board[level - i - 1][j]
        for j in range(10):
            board[0][j] = "-"

    # for i in range(18):
    #	for j in range(10):
    #		print(tetrisBoard[i][j], end = "")
    #	print()
    # print("------------------------------------------------")

    return score


# 洞洞計數器(被TetrisMovement使用)
# 輸入欲搜尋之版面，回傳製造之洞洞數量
def Holes_Quantity(board):
    holes = 0  # 存放洞洞數量
    for x in range(10):
        # print("checking x:", x)
        for y in range(18):
            # print("	checking y:", y)
            if board[y][x] == "*":
                # print("		found surface y:", y)
                for y2 in range(y, 18, 1):
                    # print("			searching holes y:", y2)
                    if board[y2][x] == "-":
                        # print("				found holes x:", y2)
                        holes += 1
                break

    return holes


# 將做一個放俄羅斯方塊的動作整合起來，會影響板上的樣子((被BadScoreCal使用))
# 回傳分數變化、最後洞的數量、放置方塊之最大高度
# ~~~~Tetris_Movement使用方法:~~~~~~
# 放置方塊，並把回傳的東西放到tetrisMovementTemp
# tetrisMovementTemp = Tetris_Movement("L", 90, 0, tetrisBoard)
# 計算最後的分數
# tetrisBoard_score += tetrisMovementTemp[0]
# 計算產生的洞洞數
# delta_holes = tetrisMovementTemp[1] - previous_holes
# 將現在洞洞的數量儲存起來，等下一次放置俄羅斯方塊使用
# previous_holes = tetrisMovementTemp[1]
# 高度存入height
# height = tetrisMovementTemp[2]

# 使用完後改變的變數:分數、洞的變化、最大高度
# print(tetrisBoard_score, delta_holes, height)
# 可用此方法列印現在之版面
# PrintBoard(tetrisBoard)
def Tetris_Movement(type, rotation, location, board):
    height = Place_TetrisBlock(type, rotation, location, board)
    delta_score = CheckBoard(board)
    holes = Holes_Quantity(board)
    return [delta_score, holes, height]


# 輸出整個版面
def PrintBoard(board):
    for i in range(18):
        for j in range(10):
            print(board[i][j], end="")
        print()


# 糟糕分數計算機(不會引響版面)
# block1 block2 為陣列 [type, rotation, location]
def BadScoreCal(board, block1, block2, holeWeight, heightWeight, scoreWeight):
    testBoard = []
    xtemp = []
    for y in range(18):
        for x in range(10):
            xtemp.append(board[y][x])
        testBoard.append(xtemp)
        xtemp = []

    tetrisMovementTemp = []  # 儲存此動作回傳的數值
    delta_score = 0  # 分數變化量
    previous_holes = Holes_Quantity(testBoard)  # 放置前洞的數量
    delta_holes = 0  # 放置後洞的變化
    height = 0  # 放置方塊的最大高度

    tetrisMovementTemp = Tetris_Movement(block1[0], block1[1], block1[2], testBoard)  # 放置方塊，並把回傳的東西放到tetrisMovementTemp
    delta_score += tetrisMovementTemp[0]  # 計算分數變化量
    delta_holes += tetrisMovementTemp[1] - previous_holes  # 計算產生的洞洞數
    height += tetrisMovementTemp[2]  # 高度存入height

    tetrisMovementTemp = Tetris_Movement(block2[0], block2[1], block2[2], testBoard)  # 放置方塊，並把回傳的東西放到tetrisMovementTemp
    delta_score += tetrisMovementTemp[0]  # 計算分數變化量
    delta_holes += tetrisMovementTemp[1] - previous_holes  # 計算產生的洞洞數
    height += tetrisMovementTemp[2]  # 高度存入height

    return delta_holes * holeWeight + height * heightWeight + -1 * delta_score // 20 * scoreWeight


# 尋找最佳動作函數(不會引響版面)
# 輸入欲測試的版面與下兩個俄羅斯方塊與倍率
# 回傳最好的放置方式
# 回傳格式為[fType, fRotation, fLocation]的陣列
def FindBestMove(board, fBlock, sBlock, holeWeight, heightWeight, scoreWeight):
    bestMove = []
    lowestBadScore = 9999999999
    tempBadScore = 0
    # 所有狀況
    for x1 in range(10):
        for x2 in range(10):
            for r1 in range(0, 271, 90):
                for r2 in range(0, 271, 90):
                    try:
                        tempBadScore = BadScoreCal(board, [fBlock, r1, x1], [sBlock, r2, x2], holeWeight, heightWeight,
                                                   scoreWeight)
                    except IndexError:  # 如果那個地方根本不能放
                        # print("Index out of range")
                        break
                    # 此動作糟糕分數與全部最佳分數(最低)
                    # print("tempBadScore:", tempBadScore)
                    # print("lowestBadScore:", lowestBadScore)

                    if tempBadScore < lowestBadScore:  # 如果現分數是全部最佳分數
                        lowestBadScore = tempBadScore  # 把這個步驟儲存起來
                        bestMove = [fBlock, r1, x1]
    # 印出此動作最佳成績
    # print("lowestBadScore:", lowestBadScore)
    return bestMove


# 俄羅斯方塊題目製造機(回傳L, J, S, Z, T, O, I)
def TetrisQuestionMaker():
    rand = (int)(random.random() * 10000000000000000 % 7)
    if rand == 0:
        return "L"
    elif rand == 1:
        return "J"
    elif rand == 2:
        return "S"
    elif rand == 3:
        return "Z"
    elif rand == 4:
        return "T"
    elif rand == 5:
        return "O"
    elif rand == 6:
        return "I"
    else:
        print("random must be 0 - 6")


# --------------------------------------------訓練函數-----------------------------------------------
# 輸入權重，回傳得到的遊戲分數
# holeWeight厭洞權重 
# heightWeight厭高權重
# scoreWeight厭分數權重
# maxMove決定分數之最少步數(沒時間玩到死)
# trialQuestion 考核這世代所用的題目(數量不對會自動生題目，但每個寶寶題目不同可能引響公正性)
# 剩下都只是用來顯示在版面上，沒有參與計算
# no 現在為第幾個寶寶
# generation 現在是第幾代
# maxNo 每帶代有幾個寶寶
# maxGeneration 這次測試有幾代
# highScore這代最高分數是啥
# bestWeights 這代最高分是誰
# weights 現在玩遊戲的寶寶之權重
# motherWeights 這世代的製造者
def GetGeneScore(holeWeight, heightWeight, scoreWeight, maxMove, trialQuestion=[], no=None, generation=None, maxNo=None,
                 maxGeneration=None, highScore=None, bestWeights=None, weights=None, motherWeights=None,
                 showProcess=True):
    # 製造俄羅斯板塊介面(TetrisBoard)，寬10高18
    # "-"為空白, "*"為有東西
    # 下面為示意圖
    # 左上角是TetrisBoard[0][0], 右下是TetrisBoard[17][9]
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # ----------
    # -----------
    # -----------
    tetrisBoard = []

    for i in range(18):
        tetrisBoard.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])

    tetrisBoard_score = 0  # tetrisBoard的分數

    if len(trialQuestion) != maxMove:  # 如果題目是不合格的，長度不足或超過
        print("Question's length must be equal to your maxMove.")
        print("Auto generating a question...")
        for blockCounter in range(maxMove):
            trialQuestion.append(TetrisQuestionMaker())

    currentBlock = trialQuestion[0]  # 此掉落之俄羅斯方塊
    nextBlock = trialQuestion[1]  # 下一個俄羅斯方塊

    time.sleep(0)

    move = []  # 儲存此版面最佳動作
    for moveCounter in range(maxMove):
        move = FindBestMove(tetrisBoard, currentBlock, nextBlock, holeWeight, heightWeight,
                            scoreWeight)  # 將算出的最佳動作存入move
        tetrisBoard_score += Tetris_Movement(move[0], move[1], move[2], tetrisBoard)[0]  # 執行最佳動作，並計算分數
        # 印出此動作的相關訊息
        # print("==============================================")
        # print("Generation:", generation, "/", maxGeneration, "( Mother:", motherWeights, ")")
        # print("No.", no, "/", maxNo, "( Weights:", weights, ")")
        # print("Moves:", moveCounter + 1, "/", maxMove)
        # PrintBoard(tetrisBoard)
        # print("Score:", tetrisBoard_score, "( HighScore:", highScore, ", Weights : ", bestWeights, ")")
        # 印出現在正在掉落(非實行動作的)，與下一個準備掉落的俄羅斯方塊
        currentBlock = nextBlock
        nextBlock = trialQuestion[moveCounter]
        # print("current:", currentBlock)
        # print("next", nextBlock)
        # print("==============================================")

        time.sleep(0)
        if tetrisBoard[2] != ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]:  # 如果從上往下數第三個有東西了
            # 提前結束，結算成績
            print([holeWeight, heightWeight, scoreWeight], " Final Score:", tetrisBoard_score, end="")
            return tetrisBoard_score

    # print("==========================================================")
    print([holeWeight, heightWeight, scoreWeight], " Final Score:", tetrisBoard_score, end="")
    # print("==========================================================")

    # 印出此寶寶的最終成績，停X秒
    time.sleep(0)
    return tetrisBoard_score


# 輸入基因，回傳每組基因的顯性數量(陣列)
# 格式為[[], [], [], ...]
def CalWeights(geneArray):
    weights = []
    for group in range(len(geneArray)):
        calWeightTemp = 0
        for gene in range(len(geneArray[group])):
            calWeightTemp += geneArray[group][gene]
        weights.append(calWeightTemp)
    return weights


# 輸入許多優秀的基因組，回傳一個充滿基因組(數量n)的陣列(基因組生出的寶寶們)
def MakeBabies(bestBabies: list, n: int):
    trialingGenes = []  # 存生出來的寶寶們
    babyA = []  # 存欲交配的基因A
    babyB = []  # 存欲交配的基因B
    # 做n個個體
    for geneCounter in range(n):
        trialingGene = []  # 個別寶寶生成器
        babyA = bestBabies[random.randint(0, len(bestBabies) - 1)]
        babyB = bestBabies[random.randint(0, len(bestBabies) - 1)]
        # 在每一組表現特徵的基因組們裡
        for groupCounter in range(len(babyA)):
            trialingGene.append(Fertilization(babyA[groupCounter], babyB[groupCounter]))  # 自交
        trialingGenes.append(trialingGene)  # 將自交產生的個體加入trialingGenes裡
    return trialingGenes


# =====================主程式========================
def GetBabyScore(babyGene, maxMove, trialQuestion, currentProcess):
    weights = CalWeights(babyGene)
    currentScore = GetGeneScore(weights[0], weights[1], weights[2], maxMove, trialQuestion)
    currentProcess.value += 1
    print(" [currentProcess:", currentProcess.value, "]")
    return currentScore


def GetBabiesScore_Multiprocessing(babies, maxMove, trialQuestion):
    pool = Pool(4)
    inputs = []
    manager = multiprocessing.Manager()
    currentProcess = manager.Value('i', 0)
    for baby in babies:
        inputs.append((baby, maxMove, trialQuestion, currentProcess))
    pool_outputs = pool.starmap(GetBabyScore, inputs)
    return pool_outputs


if __name__ == '__main__':
    # maxMove 一個遊戲結算之步數
    # maxNo 一個子代生的數量
    # maxGeneration 要生幾個世代
    # AlleleQuantity 個體之每個特徵等為基因數量
    maxMove = 100
    maxNo = 10
    maxGeneration = 5
    alleleQuantity = 5
    bestBabiesQuantity = 3
    bestBabies = []

    # 如果bestBabiesQuantity大於maxNo，將bestBabiesQuantity設為maxNo
    if bestBabiesQuantity > maxNo:
        print("bestBabiesQuantity must bes smaller than maxNo")
        print("auto set bestBabiesQuantity to maxNo")
        bestBabiesQuantity = maxNo

    print(">>>>>>>>>>>>>Training Settings<<<<<<<<<<<<")
    print("Max Moves :", maxMove)
    print("Babies per generation :", maxNo)
    print("Max Generations :", maxGeneration)
    print("Allele Quantity :", alleleQuantity)
    print("bestBabiesQuantity :", bestBabiesQuantity)
    print(">>>>>>>>>>>>>>starts in 3 second<<<<<<<<<<<<<<<<")
    time.sleep(3)

    bestBabies = Make_First_Genes(alleleQuantity, 3, bestBabiesQuantity)  # 將準備要交配的寶寶產生出來

    print("Initialize babies:", end="")
    for baby in bestBabies:
        print(CalWeights(baby), end="")
    print()

    for generationCounter in range(maxGeneration):  # 在每個子代裡
        highScore = 0  # 把子帶最高分設為0
        babies = MakeBabies(bestBabies, maxNo)  # 開始自交生寶寶

        print("Generation", generationCounter + 1, "babies:", end="")
        for baby in babies:
            print(CalWeights(baby), end="")
        print()

        # 產生篩選寶寶的題目
        trialQuestion = []
        for questionCounter in range(maxMove):
            trialQuestion.append(TetrisQuestionMaker())

        # 把所有小孩的分數算出來，照著babies的順序
        babiesScore = GetBabiesScore_Multiprocessing(babies, maxMove, trialQuestion)

        # 找到分數前bestBabiesQuantity名的寶寶，存入bestBabies
        bestBabiesIndex = []  # 存現在前幾名的索引值(bestBabies & babiesScore都通用)
        for babiesCurrentProcessIndex in range(maxNo):
            if len(bestBabiesIndex) < bestBabiesQuantity:
                bestBabiesIndex.append(babiesCurrentProcessIndex)
            else:
                smallestBestBabiesScoreIndex = None
                for babiesComparingIndex in bestBabiesIndex:
                    if smallestBestBabiesScoreIndex == None:
                        smallestBestBabiesScoreIndex = babiesComparingIndex
                    else:
                        if babiesScore[smallestBestBabiesScoreIndex] > babiesScore[babiesComparingIndex]:
                            smallestBestBabiesScoreIndex = babiesComparingIndex
                if babiesScore[babiesCurrentProcessIndex] > babiesScore[smallestBestBabiesScoreIndex]:
                    bestBabiesIndex.remove(smallestBestBabiesScoreIndex)
                    bestBabiesIndex.append(babiesCurrentProcessIndex)

        bestBabiesTemp = []
        for index in bestBabiesIndex:
            bestBabiesTemp.append(babies[index])

        print("Generation:", generationCounter + 1)
        for index in bestBabiesIndex:
            print("Best babies", CalWeights(babies[index]), ", score:", babiesScore[index])
        print("---------------------------------------------------------------------------------------------------------------------------")
        bestBabies = bestBabiesTemp

    _ = input("press any key to continue...")
