name="Priyanshu"
# string is immutable because we cannot change the characters of string once it is created because it is stored in a fixed memory location

#STRING SLICING
nameshort=name[0:3] #slicing the string from index 0 to 2 (3-1) excluding string.
print(nameshort)

character=name[1] #accessing character at index 1
print(character)

print(name[0:5]) #slicing the string from index 0 to 4 
#is same as
print(name[:5]) #slicing the string from index 0 to 4 

print(name[3:]) #slicing the string from index 3 to end of string
#is same as
print(name[3:len(name)]) #slicing the string from index 3 to end of string

print(name[0:7:2]) #slicing the string from index 0 to 6 with a step of 2 output: Piansu
print(name[-1:-3]) #slicing the string from index -1 to -3 (excluding -3)


#STRING FUNCTIONS
greeting="Good Morning, "
print(greeting+name) #string concatenation
print(greeting*3) #string repetition
print(len(greeting)) #length of string
print(name.lower()) #converts string to lowercase
print(name.upper()) #converts string to uppercase
print(name.replace("Priyanshu","Mavricx")) #replaces a substring with another substring
print(name.index("y")) #returns the index of first occurrence of a character
print(name.count("r")) #returns the count of a character in the string
print(name.isalnum()) #returns True if all characters in the string are alphanumeric
print(name.startswith("P")) #returns True if string starts with the specified substring. Case sensitive
print(name.endswith("u")) #returns True if string ends with the specified substring Case sensitive
print(name.capitalize()) #capitalizes the first character of the string
print(name.find("anshu")) #returns the index of first occurrence of a substring
print(name.split("y")) #splits the string at the specified character and returns a list of substrings
print(name.center(20)) #centers the string in a field of given width by padding with spaces
print(name.swapcase()) #swaps the case of each character in the string 
print(name.title()) #capitalizes the first character of each word in the string
print(name.encode()) #encodes the string into bytes


# Escape Sequences in Strings
print("Hello\nWorld") # \n is used to insert a new line 
print("Hello\tWorld") # \t is used to insert a tab space
print("Hello\\World") # \\ is used to insert a backslash
print("Hello\'World") # \' is used to insert a single quote
print("Hello\"World") # \" is used to insert a double quote
print("Hello\rWorld") # \r is used to insert a carriage return means cursor returns to the beginning of the line
print("Hello\bWorld") # \b is used to insert a backspace 
print("Hello\fWorld") # \f is used to insert a form feed
print("Hello\vWorld") # \v is used to insert a vertical tab
print("C:\\Users\\Priyanshu") # to print a file path we need to use double backslash
print(r"C:\Users\Priyanshu") # using r before the string to print raw string
# Raw string ignores escape sequences