def solution(scores):
    ta = scores[0][0]
    tb = scores[0][1]
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    maxb = -1
    count = 0
    for a, b in scores:
        if a > ta and b > tb:
            return -1
        if maxb <= b:
            maxb = b
            if a+b > ta + tb:
                count += 1
    return count + 1
            
        
        