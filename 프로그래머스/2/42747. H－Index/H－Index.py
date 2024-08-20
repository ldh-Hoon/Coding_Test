def solution(citations):
    answer = 0
    arr = sorted(citations, key = lambda x : -x)
    for i in range(len(arr)):
        if i >= arr[i]:
            return i
    answer = len(citations)
    return answer