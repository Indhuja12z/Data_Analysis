#Create a function check_voter_eligibility(voters) that takes a dictionary of names and ages:
#voters = {
  #  "Indhuja": 19,
  #  "Alex": 16,
 #   "Candy": 22
#}
# The function should print:
#Indhuja is eligible
#Alex is not eligible
#Candy is eligible
def check_voter_eligibility(v):
        for key,val in v.items():
                if val >=18:
                        print(key,"is eligible")
                else:
                        print(key,"is not eligible")

voters = {
    "Indhuja" : 19,
    "Alex": 16,
    "Candy":22
}
check_voter_eligibility(voters)



