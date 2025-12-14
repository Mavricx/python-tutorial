# Write a program which finds out whether a given name is present in a list or not.
names = ["Piku", "Rahul", "Anita", "Suresh", "Neha"]

name = input("Enter the name to search: ")

if name in names:
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")
