#2. Unique Even Numbers from a List
#Write a program that:
#Takes a list of numbers with duplicates
#Filters only even numbers
#Stores them in a set (to remove duplicates)
#Prints the final set

my_list=[]
my_set = set()
n=int(input("How many numbers u want to enter: ?"))
print("Enter the numbers one by one:")
for num in range(n):
     my_list.append(int(input()))
for i in my_list:
    if i % 2 == 0:
         my_set.add(i)
if len(my_set) > 0:
        print("Final Set with Even Numbers:")
        print(my_set)
else:
      print("Empty Set")
