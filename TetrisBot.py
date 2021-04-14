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

#------------------------關於基因的函數-----------------------------------
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

# 下一步製作俄羅斯方塊模擬器
# --------------------關於俄羅斯方塊的函數----------------------------

# 放置俄羅斯方塊函數
# 輸入俄羅斯方塊類型，俄羅斯方塊方向，俄羅斯方塊位置
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
		elif rotation == 90 or ratation == 270:
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
	
	# 找停下來的位置
	stop = False
	while 1:
		# 檢查每一個方塊
		for i in checkBlock:
			# 如果以碰到地板，stop = true
			if i[0] + 1 > 17:
				# print("STOP")
				stop = True
				break
			# 每一個方塊下面是不是有東西，如果有，stop = true
			elif board[i[0] + 1][i[1]] == "*":
				# print("STOP")
				stop = True
				break
		# 如果stop == false，全部方塊下去一階
		if stop == False:
			for i in checkBlock:
				i[0] = i[0] + 1
		# 如果stop == true，將"-"換成"*"(board)，並跳出迴圈
		else:
			for i in checkBlock:
				board[i[0]][i[1]] = "*"
			break


# 檢查版面函數(消行與計分)
# 會回傳此檢查所獲得的分數
def CheckBoard(board):
	# 紀錄消掉的行的編號
	cleaned = []
	# 在每一行中
	for i in range(18):
		for j in range(10):
			# 如果有一個空的，不理
			if board[i][j] == "-":
				break
		# 如果都是"*",清掉那一行並標記起來
		else:
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
			
		#for i in range(18):
		#	for j in range(10):
		#		print(tetrisBoard[i][j], end = "")
		#	print()
		#print("------------------------------------------------")
			
	return score
	
# 將做一個放俄羅斯方塊的動作整合起來
# 回傳分數變化、製造洞的數量、放置方塊之最大高度
def Tetris_Movement(type, rotation, location, board):
	Place_TetrisBlock(type, rotation, location, board)
	return CheckBoard(board)
	
# 洞洞計數器
def Holes_Quantity(board):
	# 存放洞洞數量
	holes = 0
	return holes
	
# 輸出整個版面
def PrintBoard(board):
	for i in range(18):
		for j in range(10):
			print(board[i][j], end = "")
		print()
		
# =====================主程式========================
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
    
# tetrisBoard的分數
tetrisBoard_Score = 0

	































