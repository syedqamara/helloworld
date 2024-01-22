
x = int(input("Enter number to write Table "))

is_prime = True

for num in range(2, x):
    if x % num == 0:
        is_prime = False
        break


if is_prime:
    print(str(x) + " is a Prime Number")
else:
    print(str(x) + " is not a Prime Number")
