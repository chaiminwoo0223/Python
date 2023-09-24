# 입력
number = input("정수 입력> ")

# 짝수/홀수 구분
if number[-1] in "02468":
    print("짝수")
else:
    print("홀수")