# 객체 만들기
students = [
    { "name":"윤인성", "korean":87, "math":98, "english":88 },
    { "name":"연하진", "korean":92, "math":98, "english":96 },
    { "name":"구지연", "korean":76, "math":96, "english":94 },
    { "name":"나선주", "korean":98, "math":92, "english":96 },
    { "name":"윤아린", "korean":95, "math":98, "english":98 },
    { "name":"윤명월", "korean":64, "math":88, "english":92 }
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"]
    score_avg = score_sum / 3
    print(student["name"], score_sum, score_avg, sep="\t")