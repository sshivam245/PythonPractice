maths = float(input("what is your maths score?"))
chemistry = float(input("what is your chemistry score?"))
biology= float(input("what is your biology score?"))
physics= float(input("what is your physics score?"))
computer = float(input("what is your computer score?"))

total = maths + chemistry + biology + physics + computer
print (f"your total marks are: {total} ")

percentage = float(total)*(100/500)
print(f"your percentage is: {percentage} ")


if percentage >= 90:
        print("your grade is A")
elif percentage >= 80 :
        print("your grade is B")
elif percentage >= 70 :
        print("your grade is C")
elif percentage >= 60 :
        print("your grade is D")
elif percentage >= 40:
       print("your grade is E")
else:
        print("your grade is F")

