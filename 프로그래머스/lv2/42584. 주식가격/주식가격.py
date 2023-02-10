def solution(prices):
    length = len(prices)
    answer = [length - 1 - i for i in range(length)]
    stack = []
    for i in range(length):
        while stack:
            if prices[i] < prices[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            else:
                break

        stack.append(i)

    return answer