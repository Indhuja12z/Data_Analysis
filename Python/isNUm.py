#5. Positive, Negative, or Zero Counter
#Write a function that takes a list of integers and:
#Counts how many are positive, negative, or zero
#Prints the counts
def Counter(n):
    pos=neg=z = 0
    for i in n:
        if i > 0:
            pos =pos + 1
        elif i == 0:
            z = z+1
        else :
            neg =neg +1
    return pos,neg,z
        
numbers = [1,-4,6,8,9,4,30,6,0,7,-6,-5]
p , n, z = Counter(numbers)
print("Positive: " ,p)
print("Negative: " ,n)
print("Zero: " ,z)