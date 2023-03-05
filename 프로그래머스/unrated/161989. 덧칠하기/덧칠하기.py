def solution(n, m, sections):
    sections.sort()  # sections 리스트를 정렬합니다.
    current = 0  # 현재 위치
    count = 0  # 페인트칠 횟수
    for s in sections:
        if s > current:  # 다음 영역이 현재 위치보다 오른쪽에 있을 경우
            count += 1  # 페인트칠 횟수를 증가시킵니다.
            current = s + m - 1  # 현재 위치를 페인트칠한 영역의 끝으로 갱신합니다.
    return count
