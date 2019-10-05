age = int(input("Input your age: "))

if age >= 3 and age <= 5:
    print("You should be in Early Years!")
elif age > 5 and age <= 10:
    print("You should be in Lower School!")
elif age > 10 and age <= 13:
    print("You should be in Prep School!")
elif age > 13 and age <= 16:
    print("You should be in Senior School!")
elif age > 16 and age <= 18:
    print("You should be in Sixth Form!")
else:
    print("You shouldn't be a student.")