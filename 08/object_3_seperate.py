# 객체를 처리하는 함수(2)
def create_student(name, korean, math, english):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"]

def student_get_avg(student):
    return student_get_sum(student) / 3

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_avg(student)
    )

students = [
    create_student("윤인성", 87, 98, 88),
    create_student("연하진", 92, 98, 96),
    create_student("구지연", 76, 96, 94),
    create_student("나선주", 98, 92, 96),
    create_student("윤아린", 95, 98, 98),
    create_student("윤명월", 64, 88, 92)
]

for student in students:
    print(student_to_string(student))