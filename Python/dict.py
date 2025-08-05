 #Exercise 2: Dictionary Practice
#Create a dictionary with your name, age, college, and favorite language.
#Update the language to "Python"
#Print all key-value pairs using a loop.

pupil ={
    "name" : "Indhuja",
    "age" : 19,
    "college" : "GCT",
    "lang" : "Tamil",
    "fav-prog-lang" : "java"
}
for key, value in pupil.items():
        print(key, ":",value)
pupil["fav-prog-lang"] = "Python"
for k,v in pupil.items():
        print(k, ":",v)
