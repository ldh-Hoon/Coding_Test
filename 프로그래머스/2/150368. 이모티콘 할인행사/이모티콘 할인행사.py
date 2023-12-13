def count_plus(users, emo, sales):
    count = 0
    total_earn = 0
    for u in users:
        money_count = 0
        min_sale = u[0]
        max_money = u[1]
        for i in range(len(emo)):
            if sales[i]>=min_sale:
                money_count += emo[i]*(100-sales[i])/100
            if money_count >= max_money:
                break
        if money_count >= max_money:
            count += 1
        else:
            total_earn += money_count
    return [count, total_earn]

def solution(users, emoticons):
    sale_value_list = [10, 20, 30, 40]
    max_plus_count = 0
    max_sell_money = 0  
    c = []
    all_list = [0 for i in range(len(emoticons))]
    while True:
        sale_list = []
        for l in all_list:
            sale_list.append(sale_value_list[l])
        c = count_plus(users, emoticons, sale_list)
        
        if c[0]>max_plus_count:
            max_plus_count = c[0]
            max_sell_money = c[1]
        elif c[0]==max_plus_count and c[1]>max_sell_money:
            max_sell_money = c[1]
            
        all_list[0]+=1
        check = 1
        while check!=0:
            check = 0
            for l in range(len(all_list)):
                if all_list[l]>3 and l!=len(all_list)-1:
                    all_list[l+1]+=1
                    all_list[l] = 0
                    check += 1
        if all_list[len(all_list)-1]==4:
            break;
    return [max_plus_count, max_sell_money]