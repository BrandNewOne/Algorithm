import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

board = []
for i in range(R):
    board.append(list(map(str, sys.stdin.readline().strip())))
    
N = map(int, sys.stdin.readline().strip())
hList = list(map(int, sys.stdin.readline().split()))

def makeBoard(h, sw):
    que = deque([])
    if sw:
        for idx, source in enumerate(board[h]):
            if source == 'x':
                board[h][idx] = '.'
                
                if h-1 >= 0 and board[h-1][idx] == 'x':
                    que.append((h-1, idx))
                    BFS(que)  
                if  h+1 < R and board[h+1][idx] == 'x':
                    que.append((h+1, idx))
                    BFS(que)
                if idx+1 < C and board[h][idx+1] == 'x':
                    que.append((h, idx+1))
                    BFS(que)
                       
                break
    else:
        for idx, source in enumerate(board[h][::-1]):
            if source == 'x':
                board[h][C-idx-1] = '.'
                
                if h-1 >= 0 and board[h-1][C-idx-1] == 'x':
                    que.append((h-1, C-idx-1))
                    BFS(que)
                if C-idx-2 >= 0 and board[h][C-idx-2] == 'x':
                    que.append((h, C-idx-2))
                    BFS(que)
                if h+1 < R and board[h+1][C-idx-1] == 'x':
                    que.append((h+1, C-idx-1))
                    BFS(que)
                
                break
    
    return board

def BFS(que):
    visited=set()
    rowMap = {}
    
    while que:
        row, col = que.popleft()
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        if col in rowMap:
            if rowMap[col] < row:
                rowMap[col] = row
        else:
            rowMap[col] = row
        
        if col+1 < C and board[row][col+1] == 'x':
            que.append((row,col+1))
        
        if col-1 >= 0 and board[row][col-1] == 'x':
            que.append((row,col-1))
        
        if row+1 < R and board[row+1][col] == 'x':
            que.append((row+1,col))
        
        if row-1 >= 0 and board[row-1][col] == 'x':
            que.append((row-1,col))   
    
    cntFallRowList = []
    for col, row in rowMap.items():
        cnt = 0
        for i in range(row+1,R):
            if board[i][col] == '.':
                cnt += 1
            else:
                break
        cntFallRowList.append(cnt)
        
    cntFallRow = min(cntFallRowList)
    if cntFallRow != 0:
        for row, col in visited:
            board[row][col] = '.'
        for row, col in visited:
    
            board[row+cntFallRow][col] = 'x'
    
    return board


def solution():
    sw = True
    for h in hList:
        board = makeBoard(R-h,sw)
        sw = not sw
    
    return board
    
solution()

for _ in board:
    print(''.join(s for s in _))