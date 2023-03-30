word = input()

count = 0
i = 0
while i < len(word):
    if word[i] == 'c':
        if i + 1 < len(word) and (word[i+1] == '=' or word[i+1] == '-'):
            i += 1
    elif word[i] == 'd':
        if i + 1 < len(word) and word[i+1] == 'z' and i + 2 < len(word) and word[i+2] == '=':
            i += 2
        elif i + 1 < len(word) and word[i+1] == '-':
            i += 1
    elif word[i] == 'l' and i + 1 < len(word) and word[i+1] == 'j':
        i += 1
    elif word[i] == 'n' and i + 1 < len(word) and word[i+1] == 'j':
        i += 1
    elif word[i] == 's' and i + 1 < len(word) and word[i+1] == '=':
        i += 1
    elif word[i] == 'z' and i + 1 < len(word) and word[i+1] == '=':
        i += 1
    count += 1
    i += 1

print(count)
