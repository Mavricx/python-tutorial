#create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dict={}

for i in range (2):
    name=input("Enter your name: ")
    lang=input("Enter your favorite language: ")
    dict[name]=lang
print(dict)

# Q. if the names of 2 friends are same; what will happen to the program in problem 6?

# Dictionary keys must be unique
# If the same key is entered again, the latest value replaces the old one

# Q. If languages of two friends are same; what will happen to the program in problem 6?

# Dictionary values can be duplicated
# Only keys must be unique, not values