import sys
import heapq

N = int(sys.stdin.readline().strip())
timeList = []
for i in range(N):
    S, T = map(int, sys.stdin.readline().split())
    timeList.append((S, T))

timeList = sorted(timeList, key = lambda x : (x[0], x[1]))

def solution():
    answer = 0
    roomList = [timeList[0][1]]
    
    for time in timeList[1:]:
        schedule = roomList[0]
        
        if schedule <= time[0]:
            heapq.heappop(roomList)
            heapq.heappush(roomList, time[1])
        else:
            heapq.heappush(roomList, time[1])
        
    return len(roomList)

print(solution())
