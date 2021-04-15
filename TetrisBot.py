# remember to download pyautogui moduel
# or it will not work

import random
import time

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
				# print("i[0]", i[0])
				if 18 - i[0] > height: # y方向越低越高
					height =18 - i[0]
					# print("height :", height)
			break
	return (height)

# 檢查版面函數(消行與計分)(被TetrisMovement使用)
# 會回傳此檢查所獲得的分數，並完成設定板上的消除
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
	
# 洞洞計數器(被TetrisMovement使用)
# 輸入欲搜尋之版面，回傳製造之洞洞數量
def Holes_Quantity(board):
	# 存放洞洞數量
	holes = 0
	for x in range(10):
		#print("checking x:", x)
		for y in range(18):
			#print("	checking y:", y)
			if board[y][x] == "*":
				#print("		found surface y:", y)
				for y2 in range(y, 18, 1):
					#print("			searching holes y:", y2)
					if board[y2][x] == "-":
						#print("				found holes x:", y2)
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
			print(board[i][j], end = "")
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
			
	# 儲存此動作回傳的數值
	tetrisMovementTemp = []
	# 分數變化量
	delta_score = 0
	# 放置前洞的數量
	previous_holes = Holes_Quantity(testBoard)
	# 放置後洞的變化
	delta_holes = 0
	# 放置方塊的最大高度
	height = 0

	# 放置方塊，並把回傳的東西放到tetrisMovementTemp
	tetrisMovementTemp = Tetris_Movement(block1[0], block1[1], block1[2], testBoard)
	# 計算分數變化量
	delta_score += tetrisMovementTemp[0]
	# 計算產生的洞洞數
	delta_holes += tetrisMovementTemp[1] - previous_holes
	# 高度存入height
	height += tetrisMovementTemp[2]
	
	# 放置方塊，並把回傳的東西放到tetrisMovementTemp
	tetrisMovementTemp = Tetris_Movement(block2[0], block2[1], block2[2], testBoard)
	# 計算分數變化量
	delta_score += tetrisMovementTemp[0]
	# 計算產生的洞洞數
	delta_holes += tetrisMovementTemp[1] - previous_holes
	# 高度存入height
	height += tetrisMovementTemp[2]
	
	
	return delta_holes * holeWeight + height * heightWeight + -1 * delta_score * scoreWeight
	
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
						tempBadScore = BadScoreCal(board, [fBlock, r1, x1], [sBlock, r2, x2], holeWeight, heightWeight, scoreWeight)
					except IndexError: # 如果那個地方根本不能放
						# print("Index out of range")
						break
					# 此動作糟糕分數與全部最佳分數(最低)
					# print("tempBadScore:", tempBadScore)
					# print("lowestBadScore:", lowestBadScore)
					# 如果現分數是全部最佳分數
					if tempBadScore < lowestBadScore:
						lowestBadScore = tempBadScore
						# 把這個步驟儲存起來
						bestMove = [fBlock, r1, x1]
	# 印出此動作最佳成績
	print("lowestBadScore:", lowestBadScore)		
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
def GetGeneScore(_holeWeight, _heightWeight, _scoreWeight):
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
	tetrisBoard_score = 0
	
	# 此掉落之俄羅斯方塊
	currentBlock = TetrisQuestionMaker()
	# 下一個俄羅斯方塊
	nextBlock = TetrisQuestionMaker()
	# ----------------------------player statisics--------------------------------
	holeWeight = _holeWeight
	heightWeight = _heightWeight
	scoreWeight = _scoreWeight
	
	time.sleep(0)
	move = []
	while 1:
		move = FindBestMove(tetrisBoard, currentBlock, nextBlock, holeWeight,heightWeight, scoreWeight)
		tetrisBoard_score += Tetris_Movement(move[0], move[1], move[2], tetrisBoard)[0]
		PrintBoard(tetrisBoard)
		print("Score:", tetrisBoard_score)
		
		currentBlock = nextBlock
		nextBlock = TetrisQuestionMaker()
		print("current:", currentBlock)
		print("next", nextBlock)
		print("==============================================")
		
		time.sleep(0)
		if tetrisBoard[2] != ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]:
			print("Game Over")
			print("Final Score:", tetrisBoard_score)
			return tetrisBoard_score

# 輸入基因，回傳每組基因的顯性數量(陣列)
# 格式為[[], [], [], ...]
def CalWeights(geneArray):
	weights = []
	for group in range(len(geneArray)):
		calWeightTemp = 0
		for gene in range(100):
			calWeightTemp += geneArray[group][gene]
		weights.append(calWeightTemp)
	return weights

# 輸入基因組，回傳一個充滿基因組的陣列(基因組生出的寶寶們)	
def MakeBabies(genes, n):
	trialingGenes = []
	for geneCounter in range(n):
		trialingGene = []
		for groupCounter in range(len(genes)):
			trialingGene.append(Fertilization(genes[groupCounter], genes[groupCounter]))
		trialingGenes.append(trialingGene)
	return trialingGenes
# =====================主程式========================
# 製作三個特徵基因組，格式為[holeGene, heightGene, scoreGene]
# holeGene, heightGene, scoreGene都為012所組成的陣列
motherGene = [Make_First_Gene(100), Make_First_Gene(100), Make_First_Gene(100)]

highScore = 0
bestGene = 0
babies = MakeBabies(motherGene, 3)
for baby in babies:
	Weights = CalWeights(baby)
	currentScore = GetGeneScore(Weights[0], Weights[1], Weights[2])
	if currentScore > highScore:
		highScore = currentScore
		bestGene = baby

print(CalWeights(bestGene))
print("highscore", highScore)
	
























