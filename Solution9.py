quantity = int(input("Enter quantity : "))
amount = quantity * 100

if amount >= 1000:
    amount = (amount / 100) * 90
    print("Bill amount :", amount)
else:
    print("Bill amount :", amount)
