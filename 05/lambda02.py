# 인라인 람다
list_input = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input)
print("# map() 함수의 실행 결과")
print("map(power, list_input):", output_a)
print("map(power, list_input):", list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input):", output_b)
print("filter(under_3, list_input):", list(output_b))