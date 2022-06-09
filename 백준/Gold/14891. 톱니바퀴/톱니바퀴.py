gear = []
for _ in range(4):
    gear.append(list(map(int, input())))

def roll(i, dirction):
    if dirction == 1:
        gear[i].insert(0, gear[i].pop())
    else:
        gear[i].append(gear[i].pop(0))

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    change = [a]
    for i in range(a+1, 4):
        if gear[i][6] != gear[i-1][2]:
            change.append(i)
        else:
            break

    for i in range(a-1, -1, -1):
        if gear[i][2] != gear[i+1][6]:
            change.append(i)
        else:
            break

    for c in change:
        if abs(a - c) % 2 == 0:
            roll(c, b)
        else:
            roll(c, -b)

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2**i

print(answer)