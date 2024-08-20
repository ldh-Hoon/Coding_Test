def solution(number, k):
    arr = []
    kk = k
    for n in number:
        if not arr:
            arr.append(n)
            continue
        if k > 0:
            while arr[-1] < n:
                arr.pop()
                k -= 1
                if not arr or k <= 0:
                    break
        arr.append(n)
    arr = arr[:-kk] if k > 0 else arr
    return ''.join(arr)