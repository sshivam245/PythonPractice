principle = int(input("Enter principle amount: "))
rate = int(input("Enter interest rate: "))
time = int(input("Enter time(years): "))

ci= principle * pow((1 + rate / 100), time) - principle

print("Compound interest is ",ci)
