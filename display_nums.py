t = 10
n = int(input("Enter the number of terms you want in the series: "))
i = 0
s = 0

while i < n:
    print(t)
    s = s+t
    t += 5
    i += 1
print(f"sum is {s}")
#wap to print numders till 40 and pront the sum 