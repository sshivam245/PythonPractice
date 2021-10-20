A = int(input("what is the value of A:  "))
B = int(input("what is the value of B:  "))
C = int(input("what is the value of C:  "))
s = (A + B + C) / 2
Area = (s*(s-A)*(s-B)*(s-C)) ** 0.5
print(f"area of triangle is :   {Area}")
