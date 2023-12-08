def solution(players, callings):
    table = dict()
    for i, p in enumerate(players):
        table[p] = i
    for c in callings:
        i = table.get(c)
        table[players[i]] = i-1
        table[players[i-1]] = i
        players[i] = players[i-1]
        players[i-1] = c        
    return players