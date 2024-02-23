numbers = [int(input("Enter number1 : ")),
           int(input("Enter number2 : ")),
           int(input("Enter number3 : ")),
           int(input("Enter number4 : ")),
           int(input("Enter number5 : "))]

removeElement = int(input("Enter element to remove : "))

if removeElement in numbers:
    numbers.remove(removeElement)
    print("Number deleted : ", numbers)
else:
    print("Number not found : ", numbers)