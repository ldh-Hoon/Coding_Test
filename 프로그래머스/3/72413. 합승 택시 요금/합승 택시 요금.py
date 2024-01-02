from heapq import heappop, heappush
INF = 99999999
def d(start, cost_map, n):
    cost = [INF for _ in range(n+1)]
    cost[start] = 0
    
    hq = [[start, 0]]
    while hq:
        s, c = heappop(hq)
        for near, c2 in cost_map[s]:
            if cost[near] > c2 + c:
                cost[near] = c2 + c
                heappush(hq, [near, cost[near]])
    return cost
def solution(n, s, a, b, fares):
    cost_map = [[] for _ in range(n+1)]
    for f in fares:
        cost_map[f[0]].append([f[1], f[2]])
        cost_map[f[1]].append([f[0], f[2]])
    
    answer = INF
    for mid in range(n+1):
        cost_map_from_mid = d(mid, cost_map, n)
        if answer > cost_map_from_mid[s] + cost_map_from_mid[a] + cost_map_from_mid[b]:
            answer = cost_map_from_mid[s] + cost_map_from_mid[a] + cost_map_from_mid[b]
    return answer