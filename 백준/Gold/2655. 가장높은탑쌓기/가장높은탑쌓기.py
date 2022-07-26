n = int(input())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a,b,c, i+1))
bricks.sort(key=lambda x:x[0], reverse=True)
dy = [[b[1], b[3]] for b in bricks]
for i in range(1, n):
    answer = dy[i][0]
    index = []
    for j in range(i):
        if bricks[j][2] > bricks[i][2]:
            tmp = dy[j][0] + dy[i][0]
            if answer < tmp:
                answer = tmp
                index = dy[j][1:]
    dy[i][0] = answer
    if index != 0:
        dy[i] += index

dy.sort(key=lambda x:x[0])
print(len(dy[-1])-1)
for x in dy[-1][1:]:
    print(x)