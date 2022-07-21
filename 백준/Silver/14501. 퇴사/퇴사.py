n = int(input())
meeting = []
for _ in range(n):
    a, b = map(int, input().split())
    meeting.append((a, b))
answer = 0
def DFS(day, price):
    global answer
    if day > n:
        return
    if day == n:
        if price > answer:
            answer = price
    else:
        DFS(day + meeting[day][0], price + meeting[day][1])
        DFS(day+1, price)
DFS(0, 0)
print(answer)
