

num1 = int(input("enter your 1 number!!!"))
num2 = int(input("enter your 2 number!!!"))
print("Enter which operation would you like to perform?")

perform = input("Enter any of these char for specific operation +,-,*,/: ")

if perform == '+':
    result = num1 + num2
elif perform == '-':
    result = num1 - num2
elif perform == '*':
    result = num1 * num2
elif perform== '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, perform, num2, ":", result)


