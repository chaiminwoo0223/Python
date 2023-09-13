# 다양한 형태의 부동소수점 출력하기
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)
print("기본 :", output_a)
print("15칸 만들기 :", output_b)
print("15칸에 부호 추가하기 :", output_c)
print("15칸에 부호 추가하고 0으로 채우기 :", output_d)
print()

# 소수점 아래 자릿수 지정하기
output_e = "{:+15.1f}".format(52.273)
output_f = "{:15.2f}".format(52.273)
output_g = "{:15.3f}".format(52.273)
print("소수점 1자리 표시 :", output_e)
print("소수점 2자리 표시 :", output_f)
print("소수점 3자리 표시 :", output_g)
print()

# 의미없는 소수점 제거하기
output_h = "{:g}".format(52.0)
print("의미 없는 0을 제거 :", output_h)