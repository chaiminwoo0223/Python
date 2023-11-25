# 염기의 개수
dna = input("염기 서열을 입력해주세요: ")
counter = {}

for i in range(len(dna)):
    e = dna[i]
    if e in counter:
        counter[e] += 1
    elif e == "a":
        counter[e] = 1
    elif e == "t":
        counter[e] = 1
    elif e == "g":
        counter[e] = 1
    elif e == "c":
        counter[e] = 1
        
print("a의 개수:", counter["a"])
print("t의 개수:", counter["t"])
print("g의 개수:", counter["g"])
print("c의 개수:", counter["c"])