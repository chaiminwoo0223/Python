# 해당하는 값 모두 제거하기
arr = [1, 2, 1, 2]
value = 2

while value in arr:
    arr.remove(value)
print(arr)