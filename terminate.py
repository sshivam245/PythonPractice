sum = 0
choice = input("do you wish to add a number ? Enter yes or no:")
num = int(input("enter a numbe to be addedd toether:"))
sum+=num
while choice. upper( )=="YES":
    choice = input ("DO you wish to add another number ? enter yes or no")
    if choice. upper( )== "YES":
        num = int(input("enter a number to be added together:"))
    elif choice.upper( )=="NO":
        break
    sum+=num
    print("The sum of the number given is {}". format(sum))
