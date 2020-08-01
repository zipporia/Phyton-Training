class Student:
    def __init__(self, st_name, st_age, st_grade):
        self.st_name = st_name
        self.st_age = st_age
        self.st_grade = st_grade

    def get_grade(self):
        return self.st_grade


class Course:
    def __init__(self, course_name, max_student):
        self.course_name = course_name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        else:
            print("error")
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("mark", 34, 80)
s2 = Student("boyet", 32, 79)
s3 = Student("Zipporia", 34, 90)

course = Course("English", 2)
course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())

