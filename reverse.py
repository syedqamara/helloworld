x = int(input("Enter Number to Reverse: "))

first_digit = int(x / 100)
new_x = int(x % 100)

second_digit = int(new_x / 10)

third_digit = int(new_x % 10)

#print("1st = " + str(first_digit))
#print("2nd = " + str(second_digit))
#print("3rd = " + str(third_digit))

print(str(third_digit) + str(second_digit) + str(first_digit))
