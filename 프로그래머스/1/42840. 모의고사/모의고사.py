def solution(answers):
    answer = []
    right = {1:0, 2:0, 3:0}
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            right[1] += 1
        if answers[i] == b[i%len(b)]:
            right[2] += 1
        if answers[i] == c[i%len(c)]:
            right[3] += 1
    right = sorted(right.items(), key = lambda x : -x[1])
    prev = 0
    for r, c in right:
        if prev <= c:
            prev = c
            answer.append(r)
    return answer