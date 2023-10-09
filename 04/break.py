# break 키워드
i = 0

while True:
    print("{}번째 반복문".format(i))
    i += 1
    cmd = input("종료하시겠습니까?(y/n) ")
    if cmd in ["y", "Y"]:
        print("반복을 종료합니다.")
        break