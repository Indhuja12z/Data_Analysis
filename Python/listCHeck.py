 #Exercise 1: List Practice
#Create a list of 5 subject names.
#Add one more subject.
#Remove one subject.
#Print all the subjects using a loop.
subjects = ["Tamil","English","Maths","Science","French"]
for sub in subjects:
        print(sub)
subjects.append("German")
subjects.insert(3,"Japanese")
for sub in subjects:
        print(sub)
subjects.remove("German")
subjects.pop(2)
for i in subjects:
    print(i)