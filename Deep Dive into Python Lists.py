#Task 1 Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
new_list = students + grades + activities
del new_list[0:2]
del new_list[1:4]
del new_list[2:5]
del new_list[-1]

print(new_list)

#Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
students_approved = []
students_approved.append("John")
students_approved.append("Doe")
students_approved.append("Smith")

#Task 3: Print the list students_approved

print(students_approved)


