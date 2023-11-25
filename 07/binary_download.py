# 이미지 읽어 들이고 저장하기
from urllib import request
import ssl

# SSL 인증 오류를 무시하기 위해, SSL 컨텍스트를 만든다.
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# urlopen() 함수로 한빛출판네트워크 로고를 읽는다.
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png", context=context)
output = target.read()
print(output)

file = open("output.png", "wb")
file.write(output)
file.close()