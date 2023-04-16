from itertools import product
def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    disc = list(product(discount, repeat=len(emoticons)))
    res = []
    def is_plus(dis, user):
        max_dis = user[0]
        tmp = 0
        for i in range(len(dis)):
            if dis[i] >= max_dis:
                tmp += emoticons[i] * (100 - dis[i]) // 100

        if tmp >= user[1]:
            return True
        else:
            return tmp

    for d in disc:
        total_money = 0
        total_plus = 0
        for u in users:
            if is_plus(d, u) == True:
                total_plus += 1
            else:
                total_money += is_plus(d, u)

        res.append([total_plus, total_money])
        
    res.sort(key=lambda x:x[1])
    res.sort(key=lambda x:x[0])
    res.reverse()
    return res[0]