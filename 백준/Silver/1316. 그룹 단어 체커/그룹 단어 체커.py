def is_group_word(word):
    # 각 문자의 등장 여부를 저장할 리스트
    alphabet = [False] * 26
    # 이전 문자를 저장할 변수
    prev_char = ''
    
    for char in word:
        # 현재 문자가 처음 등장한 경우
        if not alphabet[ord(char) - ord('a')]:
            # 등장 여부를 True로 변경
            alphabet[ord(char) - ord('a')] = True
            # 이전 문자를 현재 문자로 변경
            prev_char = char
        # 현재 문자가 이미 등장한 경우
        else:
            # 이전 문자와 같은 경우
            if prev_char == char:
                # 계속 진행
                prev_char = char
            # 이전 문자와 다른 경우
            else:
                # 그룹 단어가 아님
                return False
    
    # 모든 문자가 정상적으로 검사되었으므로 그룹 단어임
    return True

# 입력 받기
n = int(input())
words = []
for i in range(n):
    words.append(input())

# 그룹 단어의 개수 계산
count = 0
for word in words:
    if is_group_word(word):
        count += 1

# 결과 출력
print(count)
