def solution(routes):
    routes.sort(key=lambda x:x[1])

    answer = len(routes)
    ch = [False for _ in range(answer)]
    for i in range(len(routes)):
        if ch[i]:
            continue
        else:
            for j in range(i+1, len(routes)):
                if routes[j][0] <= routes[i][1] and not ch[j]:
                    ch[j] = True
                    answer -= 1
    return answer