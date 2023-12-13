def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1):
        d = 0
        for j in range(1, int(i ** (1/2) + 1)):
            if i%j == 0:
                d += 1
                if i//j!=j:
                    d += 1
            if d > limit:
                d = power
                break
        answer += d
    return answer