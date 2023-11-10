# 조건문으로 예외 처리하기
user_input = input("정수 입력> ")

if user_input.isdigit():
    number_input = int(user_input)
    print("원의 반지름:", number_input)
    print("원의 둘레:", 2 * 3.14 * number_input)
    print("원의 넓이:", 3.14 * number_input ** 2)
else:
    print("정수를 입력하지 않았습니다.")