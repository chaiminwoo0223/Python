# 객체를 만드는 함수(1)
def create_student(name, korean, math, english):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english
    }

students = [
    create_student("윤인성", 87, 98, 88),
    create_student("연하진", 92, 98, 96),
    create_student("구지연", 76, 96, 94),
    create_student("나선주", 98, 92, 96),
    create_student("윤아린", 95, 98, 98),
    create_student("윤명월", 64, 88, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"]
    score_avg = score_sum / 3
    print(student["name"], score_sum, score_avg, sep="\t")