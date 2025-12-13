# Write a program to accept marks of 6 students and display them in a sorted manner.
marks_list = []
for i in range(6):
    marks = int(input("Enter the marks of student: "))
    marks_list.append(marks)
marks_list.sort()
print("The sorted marks of students are: ", marks_list)