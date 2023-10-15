# 숫자의 종류
numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
counter = {}
count = 0

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
        count += 1

print(
"""
{}에서 
사용된 숫자의 종류는 {}개 입니다.
참고: {}
""".format(numbers, count, counter)
)