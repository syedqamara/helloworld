# 50 < F
# 50 > & < 60 == D
# 60 > & < 70 == C
# 70 > & < 80 == B
# 80 > & < 90 == A
# 90 > & < 100 == A+

om = int(input("Enter obtained marks: "))
tm = int(input("Enter total marks: "))

per = (om * 100)/tm

print("Percentage: " + str(per) + "%")

if 90 <= per <= 100:
    print("A+ Grade")
elif 80 <= per < 90:
    print("A Grade")
elif 70 <= per < 80:
    print("B Grade")
elif 60 <= per < 70:
    print("C Grade")
elif 50 <= per < 60:
    print("D Grade")
elif per < 50:
    print("F")
else:
    print("Invalid Marks provided")
