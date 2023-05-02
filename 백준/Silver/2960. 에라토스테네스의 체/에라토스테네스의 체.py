n, k = map(int, input().split())

# 2부터 N까지 모든 수를 배열에 저장
sieve = [True] * (n+1)

# 에라토스테네스의 체 알고리즘으로 소수를 찾고 지우기
cnt = 0
for i in range(2, n+1):
    if sieve[i]:
        cnt += 1
        if cnt == k:
            print(i)
            break
        for j in range(i*i, n+1, i):
            if sieve[j]:
                cnt += 1
                if cnt == k:
                    print(j)
                    break
            sieve[j] = False
