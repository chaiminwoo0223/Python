# 이미지 읽어 들이고 저장하기
from urllib import request

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb")
file.write(output)
file.close()