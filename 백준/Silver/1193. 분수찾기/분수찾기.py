X = int(input())
def find_n(X):
    tmp = 1
    cnt = 2
    while tmp < X:
        tmp += cnt
        cnt += 1

    if cnt % 2 == 1:
        return cnt-(tmp-X+1), tmp-X+1
    else:
        return tmp-X+1, cnt-(tmp-X+1)

print(f'{find_n(X)[0]}/{find_n(X)[1]}')