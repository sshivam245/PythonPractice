og_hour = int(input("Enter the hour (1 - 12): "))
inc = int(input("How many hours do you want to skip? "))
buff_hour = og_hour + inc

if buff_hour > 12:
    buff_hour -= 12

print("The new time is {} o'clock".format(buff_hour))