# 나누어 떨어지는 숫자
a = int(input("정수를 입력해주세요: "))

if a % 2 == 0:
    print("{}는 2로 나누어 떨어지는 숫자입니다.".format(a))
else:
    print("{}는 2로 나누어 떨어지는 숫자가 아닙니다.".format(a))

if a % 3 == 0:
    print("{}는 3으로 나누어 떨어지는 숫자입니다.".format(a))
else:
    print("{}는 3으로 나누어 떨어지는 숫자가 아닙니다.".format(a))

if a % 4 == 0:
    print("{}는 4로 나누어 떨어지는 숫자입니다.".format(a))
else:
    print("{}는 4로 나누어 떨어지는 숫자가 아닙니다.".format(a))

if a % 5 == 0:
    print("{}는 5로 나누어 떨어지는 숫자입니다.".format(a))
else:
    print("{}는 5로 나누어 떨어지는 숫자가 아닙니다.".format(a))