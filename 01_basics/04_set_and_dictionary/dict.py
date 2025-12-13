empty_dict = {}
print(empty_dict, type(empty_dict))

marks={
    "Harry": 98,
    "Rohan": 89,    
    "Skillf": 92,
    0:"Priyanshu"
}
print(marks, type(marks))

print(marks["Harry"])  # Accessing value using key
marks["Vikram"] = 96  # Adding a new key-value pair
print(marks)

#iterating through a dictionary
for key in marks:
    print(f"Marks of {key} are {marks[key]}")

print(marks.keys())    # prints all the keys
print(marks.values())  # prints all the values
print(marks.items())   # prints all the key-value pairs as tuples
marks.pop("Rohan")     # removes the key-value pair with key "Rohan"
marks.update({"Harsh": 90})  # adds a new key-value pair
print(marks.get("Harsh"))  # returns the value for key "Harsh"
marks.clear()  # removes all key-value pairs
marks.copy()   # returns a shallow copy of the dictionary




#get() Vs [] when key is not present
marks.get("Rani") # returns None since "Rani" is not a key in the dictionary 
marks["Rani"] # returns a KeyError since "Rani" is not a key in the dictionary