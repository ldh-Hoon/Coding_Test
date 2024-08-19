def solution(bridge_length, weight, truck_weights):
    answer = 0
    t = 0
    sum_w = 0
    on = [0 for _ in range(bridge_length)]
    while len(truck_weights)>0:
        out_w = on.pop(0)
        if out_w != 0:
            sum_w -= out_w
        if sum_w + truck_weights[0] <= weight:
            now_w = truck_weights.pop(0)
            sum_w += now_w
            on.append(now_w)
        else:
            on.append(0)
        t += 1
    return t + bridge_length