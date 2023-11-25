# random 모듈
import random

print("# random 모듈")
# random(): 0.0 <= x < 1.0 사이의 float를 리턴
print("- random():", random.random())
# uniform(min, max): 지정한 범위 사이의 float를 리턴
print("- uniform(10, 20):", random.uniform(10, 20))
# randrange(max): 0부터 max 사이의 int를 리턴
print("- randrange(10):", random.randrange(10))
# randrange(min, max): min부터 max 사이의 int를 리턴
print("- randrange(10, 20):", random.randrange(10, 20))
# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))
# shuffle(list): 리스트의 요소들을 랜덤하게 섞음
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
# sample(list, k=숫자): 리스트의 요소 중 k개를 선택
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))