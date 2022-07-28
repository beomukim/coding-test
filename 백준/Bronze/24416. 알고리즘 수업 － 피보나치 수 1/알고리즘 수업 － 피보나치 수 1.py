n = int(input())
f1_count = 0
f2_count = 0
def f1(n):
    global f1_count
    if n == 1 or n == 2:
        f1_count += 1
        return 1
    else:
        return f1(n-1) + f1(n-2)

def f2(n):
    global f2_count
    s = [0] * (n+1)
    s[1] = 1
    s[2] = 2
    for i in range(3, n+1):
        f2_count += 1
        s[i] = s[i-1] + s[i-2]
    return s[n]

f1(n)
f2(n)
print(f1_count, f2_count)