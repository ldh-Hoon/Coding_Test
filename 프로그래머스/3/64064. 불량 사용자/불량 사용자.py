from itertools import product

def solution(user_id, banned_id):
    answer = 0
    bad_list = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for ui in user_id:
            if len(ui) == len(banned_id[i]):
                match = 0
                for c in range(len(banned_id[i])):
                    if banned_id[i][c] != "*":
                        if banned_id[i][c] != ui[c]:
                            match += 1
                if match == 0:
                    bad_list[i].append(ui)
            else:
                continue
    result = []
    for p in product(*bad_list):
        if len(set(p)) == len(bad_list):
            flag = True
            for s in result:
                if len(s - set(p)) == 0:
                    flag = False
                    break
            if flag:
                result.append(set(p))
                    
    answer = len(result)
    return answer