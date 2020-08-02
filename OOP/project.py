name = input("Enter Name: ")
age = input("Enter Age: ")
gender = input("Enter Gender: ")

if age.isalpha():
    print("age must be a number")
else:
    if int(age) <= 0:
        print("age must be 1 and up")
    else:
        if gender != "male" and gender != "female":
            print("there is an error in your input data")
        else:
            if gender.lower() == "male" and int(age) >= 13:
                print("Hello", name, "You are handsome teenager.")
            elif gender.lower() == "female" and int(age) >= 13:
                print("Hi", name, "You are a beautiful teenager.")
            elif gender.lower() == "male" or gender.lower() == "female" and int(age) <= 12:
                print("Hello", name, "You are young")
