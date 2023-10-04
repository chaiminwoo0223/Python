# 리스트
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 리스트 연산하기
print("연결:", list_a + list_b)
print("반복:", list_a * 3)
print("길이:", len(list_a))

# 리스트 요소 추가하기
list_a.append(4)
print("리스트 뒤에 요소를 추가:", list_a)
list_a.insert(0, 0)
print("리스트 중간에 요소를 추가:", list_a)
list_a.extend([5, 6, 7, 8, 9])
print("리스트 뒤에 요소를 한번에 추가:", list_a)

# 리스트 요소 제거하기1
list_a.pop()
print("리스트 마지막 요소 제거:", list_a)
list_a.pop(1)
print("리스트 2번째 요소 제거:", list_a)
del list_a[0]
print("리스트 요소 하나를 제거", list_a)
del list_a[1:4]
print("리스트 요소 한번에 제거", list_a)
del list_a[2:]
print("2를 기준으로 오른쪽 모두 제거(포함):", list_a)
del list_a[:2]
print("2를 기준으로 왼쪽 모두 제거(불포함):", list_a)

# 리스트 제거하기2
list_b.remove(4)
print("값으로 제거:", list_b)
list_b.clear()
print("모두 제거:", list_b)