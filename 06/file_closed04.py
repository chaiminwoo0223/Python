# try except 구문 끝난 후 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()
except:
    print("오류가 발생했습니다.")

file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file_closed:", file.closed)