evenList = []
oddList = []
primeList = []

for num in range(0, 101):

    if num % 2 == 0:
        evenList.append(num)

    elif num % 2 != 0:
        oddList.append(num)

#     else:
#         for i in range(2, int(num / 2) + 1):
#             if (num % i) != 0:
#                 primeList.append(num)
#
# print(primeList)
print(evenList)
print(oddList)