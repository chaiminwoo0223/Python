numbers = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
arr = []

for number in numbers:
    if type(number) == list:
        for i in number:
            arr.append(i)
    else:
        arr.append(number)
        
print(
"""
{}를 평탄화하면
{}입니다.
""".format(numbers, arr)
)