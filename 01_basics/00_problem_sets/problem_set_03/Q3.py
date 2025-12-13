# Write a program to detect double space in a string.
str=input("Enter a String: ")
if "  " in str:
    print("Double space detected")
else:
    print("No double space detected")

# or 
print("Index of double space:",str.find("  "))  # returns -1 if not found else returns the index of first occurrence of double space