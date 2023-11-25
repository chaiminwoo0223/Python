# 염기 코돈 개수
dna = input("염기 서열을 입력해주세요: ")
counter = {}

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if codon in counter:
        counter[codon] += 1
    else:
        counter[codon] = 1

print(counter)