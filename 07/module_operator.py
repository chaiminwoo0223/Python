# 특정 요소를 추출하기
from operator import itemgetter

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
print(min(books, key=itemgetter("가격")))
print()
print("# 가장 비싼 책")
print(max(books, key=itemgetter("가격")))