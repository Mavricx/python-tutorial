# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the use
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total_percentage = (m1 + m2 + m3) / 3

if m1 >= 33 and m2 >= 33 and m3 >= 33 and total_percentage >= 40:
    print("PASS")
else:
    print("FAIL")
