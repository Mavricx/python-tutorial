#tuple and its functions
my_tuple = (1, 2, 3, 4, 5)
example=("apple", 42, 3.14, True)
print(example)
print(my_tuple)

ex1=() #empty tuple
ex2=(1) #not a tuple, just an integer within parentheses
ex3=(1,) #tuple with single element, comma is necessary


#tuple is immutable
# my_tuple[0] = 10 # This will raise an error
# Accessing elements
print(my_tuple[0])  # First element
print(my_tuple[2])  # Third element


#tuple functions
print(len(my_tuple))  # Length of the tuple
print(my_tuple.count(2))  # Count occurrences of 2
print(my_tuple.index(3))  # Index of first occurrence of 3

# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Accessing the nested tuple
print(nested_tuple[2][0])  # Accessing element from the nested tuple


# Tuple unpacking
a, b, c, d, e = my_tuple    
print(a, b, c, d, e)

# Concatenation
tuple2 = (6, 7, 8)  
combined_tuple = my_tuple + tuple2
print(combined_tuple) #outputs (1, 2, 3, 4, 5, 6, 7, 8)

# Repetition
repeated_tuple = my_tuple * 2
print(repeated_tuple)#outputs (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Slicing
sliced_tuple = my_tuple[1:4]
print(sliced_tuple) #outputs (2, 3, 4)

# Iterating through the tuple
for item in my_tuple:
    print(item)
# Note: Since tuples are immutable, methods that modify the tuple (like append, remove, etc.) do not exist for tuples.
# However, you can convert a tuple to a list, modify it, and convert it back to a tuple if needed.

# Converting tuple to list and back
temp_list = list(my_tuple)
temp_list.append(6)
my_tuple = tuple(temp_list)
print(my_tuple) #outputs (1, 2, 3, 4, 5, 6)

#membership testing
print(3 in my_tuple) #outputs True
print(10 in my_tuple) #outputs False