# 딕셔너리의 요소에 접근하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("ingredient[1]:", dictionary["ingredient"][1])
print("origin:", dictionary["origin"])
print()

# 값을 변경
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])