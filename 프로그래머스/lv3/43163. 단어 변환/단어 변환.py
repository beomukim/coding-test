def check(a, b):
    a = list(a)
    b = list(b)
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    global answer
    ch = [0] * len(words)
    answer = 0

    def dfs(word):
        global answer
        if word == target:
            answer = sum(ch)
        for i in range(len(words)):
            if check(word, words[i]) and ch[i] == 0:
                ch[i] += 1
                dfs(words[i])
                ch[i] -= 1

    dfs(begin)
    return answer