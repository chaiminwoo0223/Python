# 키워드 매개변수에 함수 전달하기
books = [{
    "제목": "컴퓨터비전",
    "가격": 10000
}, {
    "제목": "자연어처리",
    "가격": 15000
}, {
    "제목": "강화학습",
    "가격": 20000
}]

print("# 가장 저렴한 책")
print(min(books, key=lambda book: book["가격"]))
print()

print("# 가장 비싼 책")
print(max(books, key=lambda book: book["가격"]))