#step 1
classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("class list:", classmates)

#step 2
print("total students:",len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("first three:", classmates[:3])

#step 3
classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("soreted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

#step 4
teacher ={"name": "Mr.Sharma", "subject": "python","experiance":5}
print("\nTeacher profile:", teacher)

#step 5
print("subject:", teacher["subject"])
print("experiance:", teacher.get("experiance","not found"))
teacher["experiance"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("experiance")
print("Updated teacher profile:",teacher)

#step 6
roll_numbers = [1, 2, 3, 4, 5]
names = ["Aaarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers,names))
print("\nStudent directory:", student_directory)
print("Student at roll 3:", student_directory[3])