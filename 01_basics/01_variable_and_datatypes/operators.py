# 1. Arithmetic operators: +, -, *, / etc. 
# 2. Assignment operators:  =, +=, -= etc. 
# 3. Comparison operators: ==, >, >=, <,  != etc. 
# 4. Logical operators: and, or, not. 
 
 
# Arithmetic operators
a = 10
b = 5
print("Addition:", a + b)  # 15
print("Subtraction:", a - b)  # 5
print("Multiplication:", a * b)  # 50
print("Division:", a / b)  # 2.0

# Assignment operators
x = 10
x += 5  # x = x + 5
print("After +=:", x)  # 15
x -= 3  # x = x - 3
print("After -=:", x)  # 12

# Comparison operators
print("Equal to:", a == b)  # False
print("Greater than:", a > b)  # True
print("Greater than or equal to:", a >= b)  # True
print("Less than:", a < b)  # False
print("Not equal to:", a != b)  # True

# Logical operators
c = True
d = False
print("Logical AND:", c and d)  # False
print("Logical OR:", c or d)  # True
print("Logical NOT:", not c)  # False


print(not(True))


print(type(a))         #<class 'int'>
print(type(c))         # <class 'bool'>
print(type("Hello"))   #<class 'str'>
print(type(3.14))      #<class 'float'>
print(type([1, 2, 3])) #<class 'list'> . 
print(type((1, 2)))    #<class 'tuple'>
print(type({1: 'a'}))  #<class 'dict'>
print(type({1, 2, 3})) #<class 'set'>
print(type(None))     #<class 'NoneType'>

#Type casting

a="32.2"
b= float(a)  # converting string to float
print(b)      #32.2
print(type(b)) #<class 'float'>

a=int(b)      # converting float to int
print(a)      #32
print(type(a)) #<class 'int'>

a=str(a)      # converting int to string
print(a)      # "32"    
print(type(a)) #<class 'str'>

a=float("45")  # converting string to float
print(a)        #45.0   
print(type(a))  #<class 'float'>


#Use int() to convert while taking input from user as input() function takes input as string by default.