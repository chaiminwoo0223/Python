# 클래스 내부에 함수(메소드) 선언하기
class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_sum(self):
        return self.korean + self.math + self.english

    def get_avg(self):
        return self.get_sum() / 3

    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )

students = [
    Student("윤인성", 87, 98, 88),
    Student("연하진", 92, 98, 96),
    Student("구지연", 76, 96, 94),
    Student("나선주", 98, 92, 96),
    Student("윤아린", 95, 98, 98),
    Student("윤명월", 64, 88, 92)
]

for student in students:
    print(student.to_string())