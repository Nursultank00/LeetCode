#Сортим начало и концы, проходимся двумя указателями

def minMeetingRooms(intervals):
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)
    
    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)
    return res