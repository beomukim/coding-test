from collections import defaultdict
n, m = map(int, input().split())
groups = defaultdict(list)
for _ in range(n):
    name = input()
    for _ in range(int(input())):
        groups[name].append(input())

for n in groups:
    groups[n].sort()

for _ in range(m):
    name = input()
    num = int(input())
    if num == 0:
        for i in range(len(groups[name])):
            print(groups[name][i])
    else:
        for n in groups:
            if name in groups[n]:
                print(n)
                break

