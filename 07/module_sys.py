# sys 모듈
import sys

# 명령 매개변수를 출력
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램을 강제 종료
sys.exit()