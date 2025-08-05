#3. Student Score Tracker
#Create a dictionary where:
#Keys = student names
#Values = list of 3 subject marks
#Then:
#Print each student’s name and their average score.
def getAvg(s):
        for k,v in s.items():
                print(k ,":", sum(v)/len(v))

student ={
    "candy":[70,80,90],
    "teddy":[90,89,78],
    "totoro":[90,89,76]
}
getAvg(student)