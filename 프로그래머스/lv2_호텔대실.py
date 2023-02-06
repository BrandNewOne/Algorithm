import heapq

def makeTimeSet(book_time):
    timeSet = []
    for bt in book_time:
        startH, startM = bt[0].split(':')
        endH, endM = bt[1].split(':')
        timeSet.append((int(startH+startM),int(endH+endM)))
    
    return timeSet

def solution(book_time):
    book_time = makeTimeSet(book_time)
    book_time = sorted(book_time, key= lambda x : (x[0],x[1]))
    rooms = [book_time[0][1]]
    
    for bt in book_time[1:]:
        st, et = bt
        
        addCleanTime = rooms[0] + 10
        if addCleanTime%100 > 59:
            addCleanTime+=40
        
        if  addCleanTime <= st:
            heapq.heappop(rooms)
            
        heapq.heappush(rooms, et)
        
    return len(rooms)