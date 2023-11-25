# 간단한 대화 프로그램
import datetime

a = input()
now = datetime.datetime.now()

if a in "안녕하세요.":
    print("안녕하세요.")
elif "지금 몇 시" in a:
    print("지금은 {}시 입니다.".format(now.hour))
else:
    print(a)