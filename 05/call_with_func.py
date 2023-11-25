# map() 함수와 filter() 함수
def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input = [1, 2, 3, 4, 5]

output_a = map(power, list_input)
print("# map() 함수의 실행 결과")
print("map(power, list_input):", output_a)
print("map(power, list_input):", list(output_a))
print()

output_b = filter(under_3, list_input)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input):", output_b)
print("filter(under_3, list_input):", list(output_b))