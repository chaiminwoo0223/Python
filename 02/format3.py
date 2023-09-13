# format() 함수를 이용해, 문자열로 변환하기
format_a = "{} {} {}".format(1, "문자열", True)
print(format_a)

# IndexError 예외
format_b = "{} {}".format(1, 2, 3, 4, 5)
print(format_b)