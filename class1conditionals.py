import random

options = ["r","p","s"]
print("welcome to rock, paper, scissors")

# For i in range(3):

comp_choice = random.choice(options)
user_choice = str(input("chose r, p or s"))

if comp_choice == user_choice:
    print("you chose the same, chose again")
else: 
    print(f"i chose {comp_choice} and you chose {user_choice}")




