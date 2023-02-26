import sys
from collections import deque
 
# N, M = map(int, sys.stdin.readline().split())

# board = []
# for i in range(N):
#     board.append(list(map(int, sys.stdin.readline().split())))


board =[[0, 0, 0, 0, 0, 0, 0],
        [0, 2, 4, 5, 3, 0, 0],
        [0, 3, 0, 2, 5, 2, 0],
        [0, 7, 6, 2, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

def cutIceMountin():
    tempBoard = []
    for row, rowValue in enumerate(board):
        tempRow = []
        for col, colValue in enumerate(rowValue):
            if board[row][col]  != 0:
                zeroCount = 0
                if board[row-1][col] == 0:
                    zeroCount += 1
                
                if board[row+1][col] == 0:
                    zeroCount += 1
                
                if board[row][col-1] == 0:
                    zeroCount += 1
                
                if board[row][col+1] == 0:
                    zeroCount += 1
                
                if board[row][col] > zeroCount:
                    tempRow.append(zeroCount)
                else:
                    tempRow.append(board[row][col])
                
            else:
                tempRow.append(0)
        
        tempBoard.append(tempRow)
        
    for i, (t, b) in enumerate(zip(tempBoard, board)):
        for ii, (tr, br) in enumerate(zip(t, b)):
            if br != 0:
                board[i][ii] = br-tr
                

def islandNum():
    tempBoard = []
    que = deque([])
    
    for i,iv in enumerate(board):
        tempRow = []
        for j,jv in enumerate(iv):
            if jv == 0:
                tempRow.append(False)
            else:
                if not que:
                    que.append((i,j))
                    
                tempRow.append(True)
        tempBoard.append(tempRow)
    
    while que:
        row, col = que.popleft()
        if tempBoard[row][col] == False:
            continue
        
        if tempBoard[row-1][col] == True:
            que.append((row-1,col))
            
        if tempBoard[row+1][col] == True:
            que.append((row+1,col))
            
        if tempBoard[row][col-1] == True:
            que.append((row,col-1))
            
        if tempBoard[row][col+1] == True:
            que.append((row,col+1))
        
        tempBoard[row][col] = False
        
    return tempBoard

def isIsland(tempBoard):
    for i in tempBoard:
        for j in i:
            if j == True:
                return False
    return True
            
def isZeroland():
    for i in board:
        for j in i:
            if j != 0:
                return False
    
    return True

def solution():
    answer = 0
    
    
    
    while not isZeroland():
        answer += 1
        # 빙산 줄이기
        cutIceMountin()
        # 섬 몇개인지 확인
        tempBoard = islandNum()
        if not isIsland(tempBoard):
            break
        else:
            if isZeroland():
                answer = 0
                break
    
    # print(board)        
    return answer

print(solution())
        