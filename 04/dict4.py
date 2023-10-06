# 키가 존재하는지 않을 때, None을 출력하는지 확인하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
key = input("접근하고자 하는 키: ")
value = dictionary.get(key)

if value == None:
    print("값:", value)
    print("존재하지 않는 키에 접근하고 있다.")
else:
    print("값:", value)