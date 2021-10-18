a =int(input("Enter a digit: ")) #3 
b =int(input("Enter b digit: ")) #4 

### SWAPPING USING EXTRA VARIABLE
#swapping b -> 3 ...... a-> 4

## a = b ..... issue willl be a value lost 

temp = a   ### temp = 3 , a =3 
a = b      ### b = 4 , a =4 , temp =3 
b = temp 

print(f"your a number is : {a}")
print(f"your b number is : {b}")


