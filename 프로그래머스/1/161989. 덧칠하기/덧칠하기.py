def solution(n, m, section):
    answer = 1
    prev = -1
    for i in section:
        if prev == -1:
            prev = i
        elif i - prev >= m:
            prev = i
            answer+=1
    return answer