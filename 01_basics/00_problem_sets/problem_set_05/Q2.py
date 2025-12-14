# write a program to input eight numbers from the user and display all the unique numbers(once)
set1=set()
while True:
    if (len(set1))<8:
        num=int(input("Enter your number: "))
        set1.add(num)
    else:
        print("Set is Full..")
        break
print("Unique set of characters: ",set1)