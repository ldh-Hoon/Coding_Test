def solution(line):
    answer = []
    rect = []
    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            A = line[i][0]
            B = line[i][1]
            C = line[i][2]
            D = line[j][0]
            E = line[j][1]
            F = line[j][2]
            if (A*E - B*D)==0:
                continue
            else:
                X = (B*F - E*C)/(A*E - B*D)
                Y = (D*C - A*F)/(A*E - B*D)
                if X == int(X) and Y == int(Y):
                    answer.append([int(X), int(Y)])
                    print([int(X), int(Y)])
    minx = answer[0][0]
    maxx = answer[0][0]
    miny = answer[0][1]
    maxy = answer[0][1]
    for p in answer:
        minx = min(minx, p[0])
        maxx = max(maxx, p[0])
        miny = min(miny, p[1])
        maxy = max(maxy, p[1])
    for y in range(maxy-miny+1):
        rect.append(["."]*(maxx-minx+1))
    for p in answer:
        rect[p[1]-miny][p[0]-minx]="*"
    for y in range(maxy-miny+1):
        rect[y] = "".join(rect[y])
    rect = rect[::-1]
    return rect