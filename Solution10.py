salary = int(input("Enter salary : "))
years = int(input("Enter years : "))

if years >= 5:
    print("Bonus", (salary / 100) * 5)
else:
    print("Bonus", 0)