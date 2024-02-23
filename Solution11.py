marks = int(input("Enter obtained marks: "))

if marks >= 80:
    print("grade is A")
elif 60 < marks <= 80:
    print("grade is B")
elif 50 < marks <= 60:
    print("grade is C")
elif 45 < marks <= 50:
    print("grade is D")
elif 25 < marks <= 45:
    print("grade is E")
else:
    print("grade is F")