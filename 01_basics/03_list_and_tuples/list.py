list1=["apple",4,23345.34,False]
print(list1)

# Accessing elements
print(list1[0])  # First element
print(list1[2])  # Third element

# Slicing
print(list1[1:3])  # Elements from index 1 to 2
# Negative indexing
print(list1[-1])  # Last element

# Modifying elements
list1[1] = 100
print(list1)

# Appending elements
list1.append("new item")
print(list1)

# Removing elements
list1.remove(23345.34)
print(list1)

# Length of the list
print(len(list1))

# Iterating through the list
for item in list1:
    print(item)
# Nested lists
nested_list = [1, 2, [3, 4], 5]
print(nested_list[2])  # Accessing the nested list
print(nested_list[2][0])  # Accessing element from the nested list

# List methods


list1.sort()  # This will raise an error because the list contains mixed types
print(list1)
# To demonstrate sorting, let's create a new list with comparable types
num_list = [5, 2, 9, 1]
num_list.sort()
print(num_list)


# List comprehension
squared = [x**2 for x in range(5)]
print(squared)


# Copying a list
list_copy = list1.copy()
print(list_copy)




list1.sort() #updates the list to [1,2,7,8,15,21] 
list1.reverse()# updates the list to [15,21,2,7,8,1] 
list1.append(8)# adds 8 at the end of the list  
list1.insert(3,8)# This will add 8 at 3 index 
list1.pop() # Will remove the last element from the list.
list1.pop(2) #Will delete element at index 2 and return its value. 
list1.remove(21)# Will remove 21 from the list. 
list1.clear()# Clearing a list