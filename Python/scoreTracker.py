#Create a dictionary of 5 students with their marks out of 100.
#Then:
#Print students who scored above 80
#Print the average marks
#Update a student’s mark (your choice)
toppers =[]
def getAvg(s):
        for name,marks in s.items():
                if marks > 80:
                        toppers.append(name)
        avg_marks = sum(s.values())/len(s)
        return avg_marks
students ={
    "candy":70,
    "teddy":80,
    "totoro":90,
    "bunny":75,
    "amy":67
}
print("Average Marks:" ,getAvg(students))
print("Students who scored above 80:", toppers)


