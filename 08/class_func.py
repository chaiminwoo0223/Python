# 클래스 함수
class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------ 학생목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------  ------  ------")

    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english

    def get_avg(self):
        return self.get_sum() / 3

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())

Student("윤인성", 87, 98, 88)
Student("연하진", 92, 98, 96)
Student("구지연", 76, 96, 94)
Student("나선주", 98, 92, 96)
Student("윤아린", 95, 98, 98)
Student("윤명월", 64, 88, 92)
Student("김미화", 82, 86, 98)
Student("김연화", 88, 74, 78)
Student("박아현", 97, 92, 88)
Student("서준서", 45, 52, 72)

Student.print()