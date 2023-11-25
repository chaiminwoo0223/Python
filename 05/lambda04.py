# 딕셔너리 오름차순 정렬하기
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

print("# 가격 오름차순 정렬")
books.sort(key=lambda book: book["가격"])
for book in books:
    print(book)    