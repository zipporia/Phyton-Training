class Person:
    # parameterized constructor
    def __init__(self, person_name, person_age, person_gender):
        self.person_name = person_name
        self.person_age = person_age
        self.person_gender = person_gender

    def display(self):
        if self.person_age < 1 or self.person_age >= 20:
            print("age must be 1 to 19")
        else:
            if self.person_gender == 'male' and 13 <= self.person_age <= 19:
                print("hello", self.person_name, "You are a handsome teenager!")
            elif self.person_gender == 'female' and 13 <= self.person_age <= 19:
                print("hello", self.person_name, "You are a beautiful teenager!")
            elif self.person_gender == 'female' or self.person_gender == 'male' and self.person_age <= 12:
                print("hello", self.person_name, "You are too young")
            else:
                print("gender must male or female only")
    # creating object of the class


name = input('Enter name: ')
age = input('Enter age: ')
gender = input('Enter gender: ')

if age.isalpha():
    print("age must be a number")
else:
    # this will invoke parameterized constructor
    obj = Person(name, int(age), gender)
    # display result
    obj.display()
