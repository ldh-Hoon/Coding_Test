def solution(today, terms, privacies):
    answer = []
    
    today_year = int(today.split(".")[0])
    today_month = int(today.split(".")[1])
    today_date = int(today.split(".")[2])
    
    for index in range(len(privacies)):
        _term_kind = privacies[index].split(" ")[1]
        _term = 0
        for t in terms:
            if t.split(" ")[0] == _term_kind:
                _term = int(t.split(" ")[1])
        
        _privacies_year = int(privacies[index].split(".")[0])
        _privacies_month = int(privacies[index].split(".")[1])
        _privacies_date = int(privacies[index].split(" ")[0].split(".")[2])
        
        _privacies_month += _term
        while _privacies_month>12:
            _privacies_month -= 12
            _privacies_year += 1
        
        if today_year > _privacies_year:
            answer.append(index+1)
            continue
        elif today_year == _privacies_year:
            if today_month > _privacies_month:
                answer.append(index+1)
                continue
            elif today_month == _privacies_month:
                if today_date >= _privacies_date:
                    answer.append(index+1)
                    continue
    return answer