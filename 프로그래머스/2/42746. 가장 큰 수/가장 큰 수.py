def solution(numbers):
    answer = ''
    s = 0
    for n in numbers:
        if len(str(n)) > s:
            s = len(str(n))
    nums = sorted(numbers, key = lambda x : str(x)*3, reverse=True)
    for n in nums:
        answer += str(n)
    if int(answer) == 0:
        answer = "0"
    return answer