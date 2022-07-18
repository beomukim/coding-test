n = int(input())
tmp = n
answer = []
def DFS(i):
    global n
    if i >= 0:
        if 2 ** i <= n:
            answer.append(1)
            n -= 2 ** i
        else:
            answer.append(0)
        DFS(i-1)
cnt = 0
while tmp > 0:
    tmp //= 2
    cnt += 1
DFS(cnt - 1)
print(int(''.join(map(str, answer))))