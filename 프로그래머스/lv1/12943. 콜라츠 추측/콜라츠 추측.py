def solution(n):
    answer = 0
    def func(n):            
        if n % 2 == 1:      
            return 3 * n + 1
        else:               
            return n // 2   
    while True:    
        if n == 1:   
            break   
        n = func(n)  
        answer += 1
    return answer if answer < 500 else -1