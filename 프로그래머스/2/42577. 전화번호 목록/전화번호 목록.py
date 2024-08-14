def solution(phone_book):
    answer = True
    arr = dict()
    for p in phone_book:
        cc = ""
        for c in p[:-1]:
            cc += c
            if not cc in arr:
                arr[cc] = 1
    for p in phone_book:
        if p in arr:
            return False
    return True