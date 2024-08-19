def solution(clothes):
    answer = dict()
    for n, c in clothes:
        if c in answer:
            answer[c] += 1
        else:
            answer[c] = 1
    out = 1
    for c in answer:
        out *= answer[c]+1
    out -= 1
    return out