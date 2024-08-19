def solution(prices):
    arr = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                count += 1
                break
            else:
                count += 1
        arr.append(count)
    return arr