def solution(commands):
    answer = []
    n = 51
    arr = [['' for i in range(n)] for j in range(n)]
    merged_check = [[0 for i in range(n)] for j in range(n)]
    merged_count = 1
    for cc in commands:
        c = cc.split(" ")[0]  
        if c == "UPDATE":
            if len(cc.split(" "))>3:
                r = int(cc.split(" ")[1])
                c = int(cc.split(" ")[2])
                s = cc.split(" ")[3]
                arr[r][c] = s
                if merged_check[r][c]!=0:
                    for i in range(n):
                        for j in range(n):
                            if merged_check[i][j] == merged_check[r][c]:
                                arr[i][j] = s
            else:
                s = cc.split(" ")[1]
                for r in range(n):
                    for c in range(n):
                        if arr[r][c] == s:
                            arr[r][c] = cc.split(" ")[2]
        if c == "MERGE":
            r1 = int(cc.split(" ")[1])
            c1 = int(cc.split(" ")[2])
            r2 = int(cc.split(" ")[3])
            c2 = int(cc.split(" ")[4])
            if r1!=r2 or c1!=c2:
                if merged_check[r1][c1]==0 and merged_check[r2][c2]==0:
                    merged_check[r1][c1] = merged_count
                    merged_check[r2][c2] = merged_count
                    merged_count += 1
                    if arr[r1][c1]!="":
                        arr[r2][c2]=arr[r1][c1]
                    else:
                        arr[r1][c1]=arr[r2][c2]
                elif merged_check[r1][c1]!=0 or merged_check[r2][c2]!=0:
                    m1 = merged_check[r1][c1]
                    m2 = merged_check[r2][c2]
                    if arr[r1][c1]!="":
                        temp = arr[r1][c1]
                        arr[r2][c2] = temp
                        merged_check[r1][c1] = merged_count
                        merged_check[r2][c2] = merged_count
                    else:
                        temp = arr[r2][c2]
                        arr[r1][c1] = temp
                        merged_check[r1][c1] = merged_count
                        merged_check[r2][c2] = merged_count
                    for i in range(n):
                        for j in range(n):
                            if merged_check[i][j] == m1 or merged_check[i][j] == m2:
                                if(merged_check[i][j]!=0):
                                    merged_check[i][j] = merged_count
                                    arr[i][j] = temp
                    merged_count += 1
        if c == "UNMERGE":
            r = int(cc.split(" ")[1])
            c = int(cc.split(" ")[2]) 
            temp = arr[r][c]
            if merged_check[r][c]!=0:
                merged_temp = merged_check[r][c]
                for i in range(n):
                    for j in range(n):
                        if merged_check[i][j] == merged_temp:
                            arr[i][j] = ""
                            merged_check[i][j] = 0
                arr[r][c] = temp
        if c == "PRINT":
            r = int(cc.split(" ")[1])
            c = int(cc.split(" ")[2]) 
            if arr[r][c] == "":
                answer.append("EMPTY")
            else:
                answer.append(arr[r][c])
    return answer
