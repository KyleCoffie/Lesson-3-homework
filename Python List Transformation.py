#Task 1 Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

# Task 2  Calculate the average grade and display it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total = sum (grades)
count = len(grades)
print (total/count) 

#Task 3 Replace any grade below 80 with the value Failed
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2] = "failed"
grades[4] = "failed"
grades[8] = "failed"
print(grades)


