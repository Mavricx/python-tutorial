# Check that a tuple type cannot be changed in python.
my_tuple = (1, 2, 3, 4, 5)
try:
    my_tuple[0] = 10  # Attempting to change the first element
except TypeError as e:
    print("Error:", e)  # This should print an error message indicating that tuples are immutable