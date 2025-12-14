# Write a program to find the greatest of four numbers entered by the user. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d

print("Greatest number is:", greatest)
