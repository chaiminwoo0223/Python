# 정수
output_a = "{:d}".format(52)
print("기본 :", output_a)
print()

# 특정 칸에 출력하기    
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
print("5칸 :", output_b)
print("10칸 :", output_c)
print()

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print("양수 :", output_d)
print("음수 :", output_e)
print()

# 기호와 함께 출력하기
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)
print("양수 :", output_f)
print("음수 :", output_g)
print("양수 기호 부분 공백 :", output_h)
print("음수 기호 부분 공백 :", output_i)
print()

# 기호를 뒤로 밀기
output_j = "{:+5d}".format(52)
output_k = "{:+5d}".format(-52)
print("양수 기호 뒤로 밀기 :", output_j)
print("음수 기호 뒤로 밀기 :", output_k)
print()

# 기호를 앞으로 밀기
output_l = "{:=+5d}".format(52)
output_m = "{:=+5d}".format(-52)
print("양수 기호 앞으로 밀기 :", output_l)
print("음수 기호 앞으로 밀기 :", output_m)
print()

# 0으로 채우기
output_n = "{:+05d}".format(52)
output_o = "{:+05d}".format(-52)
print("양수 기호 0으로 채우기 :", output_n)
print("음수 기호 0으로 채우기 :", output_o)