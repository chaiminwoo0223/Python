# 날짜/시간과 관련된 기능을 가져온다.
import datetime

# 현재 날짜/시간을 구한다.
now = datetime.datetime.now()

# 계절 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))
else:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))