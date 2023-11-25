# urllib 모듈(1)
from urllib import request
import ssl

# SSL 인증 오류를 무시하기 위해, SSL 컨텍스트를 만든다.
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# urlopen() 함수로 구글의 메인 페이지를 읽는다.
target = request.urlopen("https://google.com", context=context)
output = target.read()
print(output)