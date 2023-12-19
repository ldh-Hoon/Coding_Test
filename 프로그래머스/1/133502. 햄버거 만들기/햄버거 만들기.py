def solution(ingredient):
    answer = 0
    prev = 0
    again = True
    start = 0
    end = len(ingredient)
    while again:
        again = False
        for i in range(start, end):
            if not prev == 3 and ingredient[i] == 1:
                prev = 1
                start = i - 4
                if start < 0:
                    start = 0
                continue
            elif prev == 1 and ingredient[i] == 2:
                prev = 2
                continue
            elif prev == 2 and ingredient[i] == 3:
                prev = 3
                continue
            elif prev == 3 and ingredient[i] == 1:
                again = True
                prev = 0
                answer += 1
                del ingredient[i-3 : i+1]
                end = len(ingredient)
                break
            else:
                prev = 0
                continue
    return answer