import pyautogui
import time

# 按下開始鍵後，讀取那個俄羅斯方塊
# 將俄羅斯方塊讀取後，找出最佳的放法
# 執行最佳的放法
# Game link:https://www.freetetris.org/game.php


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
# 放置方塊，並把回傳的東西(陣列形式)放到tetrisMovementTemp
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


# 糟糕分數計算機(不會引響版面)(被FindBestMove使用)
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


# T:(244, 242, 0)
# I:(245, 112, 0)
# O:(247, 36, 0)
# Z:(0, 244, 0)
# J:(197, 57, 247)
# S:(87, 195, 245)
# L:(4, 49, 247)
def scan_next_block(scan_x, scan_y):
    im = pyautogui.screenshot()
    color = im.getpixel((scan_x, scan_y))
    if color == (244, 242, 0):
        return "T"
    elif color == (245, 112, 0):
        return "I"
    elif color == (247, 36, 0):
        return "O"
    elif color == (0, 244, 0):
        return "Z"
    elif color == (197, 57, 247):
        return "J"
    elif color == (87, 195, 245):
        return "S"
    elif color == (4, 49, 247):
        return "L"


# start_vertical_location 從0開始數
def vertical_movement(location, start_vertical_location):
    if location < start_vertical_location:
        for _ in range(start_vertical_location - location):
            pyautogui.press('left')
    else:
        for _ in range(location - start_vertical_location):
            pyautogui.press('right')


def real_placing(type, rotation, location):
    if type == "T":
        if rotation == 0:
            vertical_movement(location, 3)
        elif rotation == 90:
            pyautogui.press('up')
            vertical_movement(location, 3)
        elif rotation == 180:
            for _ in range(2):
                pyautogui.press('up')
            vertical_movement(location, 3)
        elif rotation == 270:
            for _ in range(3):
                pyautogui.press('up')
            vertical_movement(location, 4)
    elif type == "I":
        if rotation == 0:
            vertical_movement(location, 3)
        elif rotation == 90:
            pyautogui.press('up')
            vertical_movement(location, 4)
    elif type == "O":
        vertical_movement(location, 4)
    elif type == "Z":
        if rotation == 0:
            vertical_movement(location, 3)
        elif rotation == 90:
            pyautogui.press('up')
            vertical_movement(location, 4)
    elif type == "J":
        if rotation == 0:
            vertical_movement(location, 3)
        elif rotation == 90:
            pyautogui.press('up')
            vertical_movement(location, 3)
        elif rotation == 180:
            for _ in range(2):
                pyautogui.press('up')
            vertical_movement(location, 3)
        elif rotation == 270:
            for _ in range(3):
                pyautogui.press('up')
            vertical_movement(location, 4)
    elif type == "S":
        if rotation == 0:
            vertical_movement(location, 3)
        elif rotation == 90:
            pyautogui.press('up')
            vertical_movement(location, 4)
    elif type == "L":
        if rotation == 0:
            vertical_movement(location, 3)
        elif rotation == 90:
            pyautogui.press('up')
            vertical_movement(location, 3)
        elif rotation == 180:
            for _ in range(2):
                pyautogui.press('up')
            vertical_movement(location, 3)
        elif rotation == 270:
            for _ in range(3):
                pyautogui.press('up')
            vertical_movement(location, 4)
    pyautogui.press('space')

# 輸入權重
hole_weight = input("請輸入洞洞權重: ")
height_weight = input("請輸入高度權重: ")
score_weight = input("請輸入分數權重: ")
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

# 將版面歸零
for i in range(18):
    tetrisBoard.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])

# 列印版面
PrintBoard(tetrisBoard)
# 三秒時間將滑鼠指標移到偵測下一個方塊的位置
input("你有兩秒的時間將滑鼠指標指到偵測下一個方塊的位置，按下Enter繼續")
time.sleep(2)
# 決定偵測下一個方塊的位置，存入detect_next_block_location(格式為(x, y))
detect_next_block_location = pyautogui.position()
print("偵測位置", detect_next_block_location)
# 偵測下一個方塊，放入next_block
next_block = scan_next_block(detect_next_block_location[0], detect_next_block_location[1])
print("next_block:", next_block)
# 按下Enter開始迴圈
input("當第一個方塊開始掉落前，按下Enter，倒數五秒後開始迴圈(請確保掉落後才開始迴圈)")
time.sleep(5)
while True:
    print("===============================================================================")
    current_Block = next_block
    next_block = scan_next_block(detect_next_block_location[0], detect_next_block_location[1])
    # 將現在版面最棒的步驟放入currentBestMove(不引響版面)
    currentBestMove = FindBestMove(tetrisBoard, current_Block, next_block, int(hole_weight), int(height_weight), int(score_weight))
    # 將回傳物列印出來
    print(currentBestMove)
    # 在虛擬版面中放置方塊
    Tetris_Movement(currentBestMove[0], currentBestMove[1], currentBestMove[2], tetrisBoard)
    # 在實際版面中放置方塊
    real_placing(currentBestMove[0], currentBestMove[1], currentBestMove[2])
    # 列印方塊
    PrintBoard(tetrisBoard)
    # 停止一下，防止太快遊戲出錯
    time.sleep(0.5)

