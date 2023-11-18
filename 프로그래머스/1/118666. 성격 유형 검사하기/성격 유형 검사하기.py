from collections import defaultdict
def solution(survey, choices):
    answer = ''
    result = defaultdict(int)
    result['R'] = 0
    result['T'] = 0
    result['C'] = 0
    result['F'] = 0
    result['J'] = 0
    result['M'] = 0
    result['A'] = 0
    result['N'] = 0
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        tmp = c - 4
        if tmp < 0:
            result[s[0]] += -tmp
        else:
            result[s[1]] += tmp
    print(result)
    if result['R'] < result['T']:
        answer += 'T'
    else:
        answer += 'R'
    if result['C'] < result['F']:
        answer += 'F'
    else:
        answer += 'C'
    if result['J'] < result['M']:
        answer += 'M'
    else:
        answer += 'J'
    if result['A'] < result['N']:
        answer += 'N'
    else:
        answer += 'A'
    
    return answer