principle = float(input("Enter principle amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time(years): "))

ci= principle * pow((1 + rate / 100), time) - principle

print("Compound interest is ",ci)
