import sys
sys.setrecursionlimit(int(10e7))
def solution(enroll, referral, seller, amount):
    amount = [a * 100 for a in amount]
    result = {}
    up = {}
    for i in range(len(enroll)):
        result[enroll[i]] = 0
        up[enroll[i]] = referral[i]
        
    
    def add(name, money):
        result[name] += money - (money // 10)
        if up[name] != "-" and money // 10 > 0:
            add(up[name], (money // 10))
            
    for i in range(len(seller)):
        add(seller[i], amount[i])
    return list(result.values())