# urllib 모듈
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽는다.
target = request.urlopen("https://google.com")
output = target.read()
print(output)