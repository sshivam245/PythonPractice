num = int(input("enter a number: "))
s_even = s_odd = 0
x=1
while x <= num:
    if x%2==0:
        s_even+=x
    else:
        s_odd+=x
    x=x+1

print("sum of even number is: ",s_even)
print("sum of odd number is: ",s_odd)