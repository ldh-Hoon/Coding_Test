INF = 9999999
def d(prevx, prevy, nowx, nowy, m, cost_map):
    if nowx == 0 and nowy == 0:
        if m[nowy][nowx+1] == 0:
            cost_map[nowy][nowx+1] = 100
            d(nowx, nowy, nowx+1, nowy, m, cost_map)
        if m[nowy+1][nowx] == 0:
            cost_map[nowy+1][nowx] = 100
            d(nowx, nowy, nowx, nowy+1, m, cost_map)
    else:
        if nowx + 1 < len(m[nowy]):
            if m[nowy][nowx+1] == 0 :
                if prevx == nowx:
                    if cost_map[nowy][nowx+1] >= cost_map[nowy][nowx] + 600:
                        cost_map[nowy][nowx+1] = cost_map[nowy][nowx] + 600
                        d(nowx, nowy, nowx+1, nowy, m, cost_map)
                else:
                    if cost_map[nowy][nowx+1] >= cost_map[nowy][nowx] + 100:
                        cost_map[nowy][nowx+1] = cost_map[nowy][nowx] + 100
                        d(nowx, nowy, nowx+1, nowy, m, cost_map)
        if nowy + 1 < len(m):
            if m[nowy+1][nowx] == 0:
                if prevy == nowy:
                    if cost_map[nowy+1][nowx] >= cost_map[nowy][nowx] + 600:
                        cost_map[nowy+1][nowx] = cost_map[nowy][nowx] + 600
                        d(nowx, nowy, nowx, nowy+1, m, cost_map)
                else:
                    if cost_map[nowy+1][nowx] >= cost_map[nowy][nowx] + 100:
                        cost_map[nowy+1][nowx] = cost_map[nowy][nowx] + 100
                        d(nowx, nowy, nowx, nowy+1, m, cost_map)
        if nowx - 1 >= 0:
            if m[nowy][nowx-1] == 0 :
                if prevx == nowx:
                    if cost_map[nowy][nowx-1] >= cost_map[nowy][nowx] + 600:
                        cost_map[nowy][nowx-1] = cost_map[nowy][nowx] + 600
                        d(nowx, nowy, nowx-1, nowy, m, cost_map)
                else:
                    if cost_map[nowy][nowx-1] >= cost_map[nowy][nowx] + 100:
                        cost_map[nowy][nowx-1] = cost_map[nowy][nowx] + 100
                        d(nowx, nowy, nowx-1, nowy, m, cost_map)
        if nowy - 1 >= 0:
            if m[nowy-1][nowx] == 0:
                if prevy == nowy:
                    if cost_map[nowy-1][nowx] >= cost_map[nowy][nowx] + 600:
                        cost_map[nowy-1][nowx] = cost_map[nowy][nowx] + 600
                        d(nowx, nowy, nowx, nowy-1, m, cost_map)
                else:
                    if cost_map[nowy-1][nowx] >= cost_map[nowy][nowx] + 100:
                        cost_map[nowy-1][nowx] = cost_map[nowy][nowx] + 100
                        d(nowx, nowy, nowx, nowy-1, m, cost_map)
def solution(board):
    cost_map = [[INF for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    cost_map[0][0] = 0
    d(0, 0, 0, 0, board, cost_map)

    return cost_map[len(board)-1][len(board[0])-1]