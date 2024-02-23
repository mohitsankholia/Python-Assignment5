classes = int(input("Enter numbers of classes: "))
attendance = int(input("Enter numbers of attendance: "))
attendancePercentage = (attendance / classes) * 100

if attendancePercentage >= 75:
    print("attendance percentage is :", attendancePercentage, ", he is allowed to sit in exam")

else:
    print("attendance percentage is :", attendancePercentage, ", he is not allowed to sit in exam")
