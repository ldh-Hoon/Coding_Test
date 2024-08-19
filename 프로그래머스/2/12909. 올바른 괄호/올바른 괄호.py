def solution(s):
    answer = True
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
        
    if count == 0:
        return True
    return False