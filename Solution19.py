dataList = [1, 'apple', 3.14, 'banana', 5, 6.7, 'orange', 8, 9]

intList = []
stringList = []
floatList = []

for values in dataList:
    if isinstance(values, int):
        intList.append(values)
    elif isinstance(values, float):
        stringList.append(values)
    elif isinstance(values, str):
        floatList.append(values)

print("List of Integers:", intList)
print("List of Strings:", stringList)
print("List of Floats:", floatList)