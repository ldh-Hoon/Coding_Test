import math
import itertools
def get(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def solution(numbers):
    answer = 0
    answers = []
    nums = [n for n in numbers]
    kinds = []
    for i in range(1, len(numbers)+1):
        kinds += list(map(''.join, itertools.permutations(nums, i)))
    print(kinds)
    for n in kinds:
        if n[0] == '0':
            continue
        if n == '1':
            continue
        if get(int(n)):
            if not n in answers:
                answers.append(n)
                answer += 1
    return answer