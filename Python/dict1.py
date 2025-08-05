# Create a dictionary with 3 keys: name, dept, and year
# Then:
# 1. Add a key "cgpa" with value 8.6
# 2. Update year to 4
# 3. Remove the dept
# 4. Print the final dictionary
student = {
    "name" : "Candy",
    "dept": "IT",
    "year": 3
}
for k,v in student.items():
        print(k, ";",v)
student["cgpa"] =8.6
student["year"] =4
del student["dept"]
for k,v in student.items():
        print(k, ";",v)
