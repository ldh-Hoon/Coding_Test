def solution(sequence, k):
    answer = []
    sum = sequence[0]
    start = 0
    end = 0
    while start <= end:
        if k > sum:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
        elif k == sum:
            answer.append([start, end])
            sum -= sequence[start]
            start += 1
        elif k < sum:
            sum -= sequence[start]
            start += 1
    min = 99999999
    out = []
    for a in answer:
        if (a[1]-a[0] + 1) < min:
            min = a[1]-a[0] + 1
            out = a
    return out