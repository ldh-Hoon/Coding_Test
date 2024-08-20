import itertools
def solution(k, dungeons):
    answer = -1
    arr = [i for i in range(len(dungeons))]
    kinds = itertools.permutations(arr, len(arr))
    max_d = 0
    for aa in kinds:
        d = 0
        now_k = k
        for a in aa:
            if now_k >= dungeons[a][0]:
                now_k -= dungeons[a][1]
                d += 1
            else:
                break
        if d > max_d:
            max_d = d
    return max_d