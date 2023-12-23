def check(num, index, must_be_zero, level):
    if index<0 or index>len(num)-1:
        return 0
    if num[index]=="1" and must_be_zero==1:
        return -1
    
    if num[index]=="1":
        must_be_zero=0
    else:
        must_be_zero=1
    
    if index%2==0:
        return 0
    return check(num, int(index - level), must_be_zero, level/2) + check(num, int(index + level), must_be_zero, level/2)
    

def solution(numbers):
    answer = []
    for n in numbers:
        num = ""
        count = 0
        num = bin(n).split("b")[1]
        count = len(num)
        fulltree = 0    
        fulltree_temp = 0
        while count-fulltree>0:
            fulltree += pow(2,fulltree_temp)
            fulltree_temp += 1
        
        while count-fulltree<0:
            num = "0"+num
            fulltree -= 1
        
        index = int(len(num)/2)
        if check(num, index, 0, int((index+1)/2)) == 0:
            answer.append(1)
        else:
            answer.append(0)    
    return answer