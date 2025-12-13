# Write a program to sum a list with 4 numbers
liw = []
for i in range(4):
    num = int(input("Enter a number: "))
    liw.append(num)
total = sum(liw)
print("The sum of the numbers is: ", total)