# urllib 모듈(2)
from urllib import request

target=request.urlopen("http://google.com")
output=target.read()
print(output)