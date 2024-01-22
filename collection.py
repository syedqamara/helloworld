
x = int(input("Enter Limit to find Sum of Natural Number from Zero to This: "))

sum = 0

for num in range(0, x):  # Range from 1 to 4 (5 is not included)
    print(str(num))
    sum = sum + num

print("Total: " + str(sum))

