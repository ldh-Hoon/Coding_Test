def solution(sizes):
    answer = 0
    max_x = 0
    max_y = 0
    for x, y in sizes:
        if x > y:
            a = x
            b = y
        else:
            a = y
            b = x
        if max_x < a:
            max_x = a
        if max_y < b:
            max_y = b
    return max_x * max_y