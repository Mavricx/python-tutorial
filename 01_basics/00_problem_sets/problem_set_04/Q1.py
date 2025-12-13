# Write a program to store seven fruits in a list entered by the use
fruit_list=[]
for i in range(7):
    fruit=input("Enter the fruit name: ")
    fruit_list.append(fruit)
print("The fruits you entered are: ")
for fruit in fruit_list:
    print(fruit)