def solution(food):
    answer = ''
    foodnum = 1
    for f in food[1:]:
        count = 0
        if f%2 != 0:
            count = f - 1
        else:
            count = f
        for _ in range(int(count/2)):
            answer += str(foodnum)
        foodnum += 1
    answer += "0" + answer[::-1]
    return answer