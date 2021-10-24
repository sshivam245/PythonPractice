english_marks = float(input("how much marks did you get in english:  "))
ip_marks = float(input("how much marks did you get in ip:  "))
eco_marks = float(input("how much marks did you get eco:  "))
maths_marks = float(input("how much marks did you get maths:  "))
polsci_marks = float(input("how much marks did you get polsci:  "))

sum = english_marks + ip_marks + eco_marks + maths_marks + polsci_marks 

avg = sum/5
print(f"your avg is:  {avg}")
