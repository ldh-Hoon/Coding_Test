def solution(s):
    answer = []
    table = dict()
    index = 0
    for c in s:
        if not c in table:
            table[c] = index
            answer.append(-1)
        else:
            answer.append(index - table[c])
            table[c] = index
        index += 1
    return answer