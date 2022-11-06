def solution(n, stages):
    fail = {i+1:0 for i in range(n+1)}

    for stage in stages:
        fail[stage] += 1
    failure = {i+1:0 for i in range(n)}
    total = len(stages)
    for i in range(n):
        failure[i+1] = fail[i+1] / total
        total -= fail[i+1]
        if total == 0:
            break

   
    return(sorted(failure, key=lambda x : failure[x], reverse=True))