def cul(k, nn, reqs):
    wait = 0
    end = [[] for _ in range(k)]
    for r in reqs:
        i = r[2] - 1
        if len(end[i]) < nn[i]:
            end[i].append(r[0] + r[1])
        else:
            if end[i]:
                min_end_time = min(end[i])
                wait += max(0, min_end_time - r[0])
                end[i].remove(min_end_time)
                end[i].append(max(r[0], min_end_time) + r[1])
    return wait

def solution(k, n, reqs):
    nn = [1 for _ in range(k)]
    minwait = cul(k, nn, reqs)
    while sum(nn) < n:
        minindex = -1
        for i in range(k):
            temp = nn[:]
            temp[i] += 1
            wait = cul(k, temp, reqs)
            if wait < minwait:
                minwait = wait
                minindex = i
        
        if minindex != -1:
            nn[minindex] += 1
        else:
            break
    return minwait