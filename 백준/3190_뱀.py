import sys
from collections import deque


N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
board = [list(0 for _ in range(N)) for _ in range(N)]

snake = deque([(0,0)])
snakeSet = set()

moveDirect = {'r':(0,1), 'l':(0,-1), 'u':(-1,0), 'd':(1,0)}

for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    board[row-1][col-1] = 1

L = int(sys.stdin.readline().strip())

def setMove(moveState, dir):
    result = ''
    if moveState == 'r':
        if dir == 'D':
            result = 'd'
        elif dir == 'L':
            result = 'u'
            
    elif moveState == 'l':
        if dir == 'D':
            result = 'u'
        elif dir == 'L':
            result = 'd'
            
    elif moveState == 'u':
        if dir == 'D':
            result = 'r'
        elif dir =='L':
            result = 'l'
            
    elif moveState == 'd':
        if dir == 'D':
            result = 'l'
        elif dir == 'L':
            result = 'r'
            
    return result

def moveSnake(moveCount, moveState):
    nextRow = snake[0][0] + moveDirect[moveState][0]
    nextCol = snake[0][1] + moveDirect[moveState][1]
    
    if ((nextRow, nextCol) in snakeSet) or (nextRow < 0 or nextRow >= N or nextCol < 0 or nextCol >= N):
        print(moveCount)
        exit() 
    elif board[nextRow][nextCol] == 0:
        snakeSet.discard(snake.pop())
    else:
        board[nextRow][nextCol] = 0
    
    snakeSet.add((nextRow, nextCol))
    snake.appendleft((nextRow, nextCol))
    
    return moveCount
    
def solution():
    moveCount = 0
    moveState = 'r'
    for _ in range(L):
        X, C = map(str, sys.stdin.readline().split())
        X = int(X)
        
        for m in range(X-moveCount):
            moveCount = moveSnake(moveCount+1, moveState)
            
        moveState = setMove(moveState, C)
        
    while True:
        moveCount = moveSnake(moveCount+1, moveState)

print(solution())