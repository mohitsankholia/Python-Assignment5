outputList = []
for i in range(0, 51):
    if i % 3 == 0 and i % 5 == 0:
        outputList.append("fizzbuzz")
    elif i % 3 == 0:
        outputList.append("fizz")
    elif i % 5 == 0:
        outputList.append("buzz")
    else:
        outputList.append(i)

print(outputList)