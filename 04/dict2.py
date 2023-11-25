# 딕셔너리에 요소 추가하기
dictionary = {"soul": "건전한 영혼", "mind": "건전한 정신"}
print("요소 추가 이전:", dictionary)
dictionary["body"] = "건전한 신체"
print("요소 추가 이후:", dictionary)

# 딕셔너리에 요소 제거하기
del dictionary["mind"]
print("요소 제거 이후:", dictionary)