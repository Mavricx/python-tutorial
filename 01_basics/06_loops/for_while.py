i = 0 
while i < 5: # print "Harry" – 5 times! 
    print("Priyanshu")     
    i = i + 1


# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
l = [1, 7, 8] 
for item in l: 
    print(item) # prints 1, 7 and 8


s = "hello"

for char in s:
    print(char)


#range function in python
# The range() function in python is used to generate a sequence of number. 
# We can also specify the start, stop and step-size as follows:
for i in range(0,7): # range(7) can also be used. 
    print(i) # prints 0 to 6

#for loop with else
# An optional else can be used with a for loop if the code is to be executed when the loops exhausts
l= [1,7,8] 
for item in l: 
    print(item) 
else: 
    print("done") # this is printed when the loop exhausts! 

#DIFFERENT STATEMENTS IN LOOP

#1.break: ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now
for i in range (0,80): 
    print(i)     # this will print 0,1,2 and 3 
    if i==3:
        break

#2.continue: ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.
for i in range(4): 
    print("printing") 
    if i == 2:   # if i is 2, the iteration is skipped  
        continue 
    print(i)

#3.pass: pass is a null statement in python. It instructs to “do nothing”
l = [1,7,8] 
for item in l: 
    pass          # without pass, the program will throw an error