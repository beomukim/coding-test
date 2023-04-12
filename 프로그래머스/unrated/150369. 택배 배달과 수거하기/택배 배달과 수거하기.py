def solution(cap, n, deliveries, pickups):
    idps = [(i, d, p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1) if d or p]
    delivery = 0
    pickup = 0
    answer = 0
    while idps:
        i, d, p = idps.pop()
        # -2 -4
        # -1 0
        # 2, 0
        # -2, -4
        # -2, -1
        # 1-, -1

        delivery += d 
        pickup += p
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += i*2
    return answer