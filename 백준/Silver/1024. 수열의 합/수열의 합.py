N, L = map(int, input().split())

# 수열의 길이 L을 고정시키고, 수열의 첫 번째 원소를 x로 놓고 수열을 생성한다.
# 수열의 합은 (x + (x+1) + (x+2) + ... + (x+L-1)) = Lx + (L-1)L/2 이다.
# 따라서 수열의 합을 S라 할 때, x = (S - (L-1)L/2) / L이 된다.
for l in range(L, 101):
    x = (N - (l-1)*l//2) // l
    if x < 0:  # x가 음수일 경우, 수열의 합이 N보다 커지므로 조건에 맞는 수열이 존재하지 않는다.
        continue
    if N == x*l + (l-1)*l//2:  # 수열의 합이 N과 일치하는 경우, 수열을 출력한다.
        print(' '.join(str(i) for i in range(x, x+l)))
        break
else:
    print(-1)
