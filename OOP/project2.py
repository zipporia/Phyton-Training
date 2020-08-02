class Choices:
    def __init__(self, chosen):
        self.chosen = chosen.upper()

        if self.chosen.lower() == 'a':
            print(f'You have chosen [{self.chosen}] - Cube')
        elif self.chosen.lower() == 'b':
            print(f'You have chosen [{self.chosen}] - Prism')
        elif self.chosen.lower() == 'c':
            print(f'You have chosen [{self.chosen}] - Cylinder')
        else:
            print("Please input a, b and c only!")

    def get_cube(self):
        cube_length = input("Enter the Length: ")
        print("Result", float(cube_length) ** 3)

    def get_prism(self):
        length = input("Enter the length: ")
        height = input("Enter the Height: ")
        width = input("Enter the width: ")
        print("Result", (float(length) * float(width)) * float(height))

    def get_cylinder(self):
        radius = input("Enter Base Radius: ")
        height = input("Enter Height: ")
        print("Result", 3.1416*((float(radius)**2) * float(height)))


print("Hello People this program calculate volumes of three shapes")
print("[A] - Cube / [B] - Prism / [C] - Cylinder")
choice = input("Enter choice here: ")

ch = Choices(choice)

if ch.chosen == "A":
    ch.get_cube()
elif ch.chosen == "B":
    ch.get_prism()
elif ch.chosen == "C":
    ch.get_cylinder()

