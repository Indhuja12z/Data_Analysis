#Exercise 2: Sum of N Natural Numbers
#Use a while loop to calculate the sum of numbers from 1 to N.
#(Take N as input from user)
sum =0
n = int(input("Enter a number"))
for i in range(n+1):
    sum = sum + i
print("The Sum is:",sum)
# --------------------------------------
j =0
while j<=n:
    sum = sum +j
    j= j+1
print("The Sum is:",sum)
