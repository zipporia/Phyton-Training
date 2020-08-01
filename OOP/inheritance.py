class Person:
    def __init__(self, f_name, f_age):
        self.name = f_name
        self.age = f_age

    def printname(self):
        print(self.name, self.age)


class Ability(Person):
    def __init__(self, f_name, f_age, year):
        super() .__init__(f_name, f_age)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.name, "you are", str(self.age), "years old. Class of", self.graduation_year)


p1 = Ability("Mark", 33, 2020)
p1.welcome()
