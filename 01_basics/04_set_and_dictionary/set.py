#set in python
my_set={1,2,3,4,5,5,5,5,5,"hello","hello"}
print(my_set)

empty_set=set()
print(empty_set, type(empty_set))

#functions of set
my_set.add(6)

my_set.remove(3)  # raises an error if element not found

my_set.discard(10)  # does not raise an error if element not found   
my_set.pop()  # removes and returns an arbitrary element from the set
my_set.union({7,8,9})  # returns a new set with elements from both sets
my_set.intersection({4,5,6,7})  # returns a new set with elements common to both sets
my_set.symmetric_difference({5,6,7,8})  # returns a new set with elements in either set but not in both
new_set=my_set.update({10,11,12})  # adds elements from another set to my_set
my_set.difference({4,5})  # returns a new set with elements in my_set but not in the other set

print(len(my_set))

print(4 in my_set)
  # membership test

print(type(my_set))

for item in my_set:
    print(item)

my_set.clear()  # removes all elements from the set
print(my_set)
