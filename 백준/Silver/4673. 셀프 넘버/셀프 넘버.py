def d(n):
    return n + sum(map(int, str(n)))

self_numbers = set(range(1, 10001))
for i in range(1, 10001):
    self_number_candidate = d(i)
    while self_number_candidate <= 10000:
        self_numbers.discard(self_number_candidate)
        self_number_candidate = d(self_number_candidate)

for self_number in sorted(self_numbers):
    print(self_number)
