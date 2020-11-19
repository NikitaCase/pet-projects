'''
word ="mountain"

letter_lc = [letter for letter in word]
print(letter_lc)

upper_lc =[letter.upper() for letter in word]
print(upper_lc)

july_temp = [30, 32, 28, 27, 26]

hot_lc = [temperature for temperature in july_temp if temperature > 27]
print(hot_lc)
'''

names = []
for word in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

lower_lc = [n.lower() for n in names]
print(lower_lc)
# @TODO: Use a list comprehension to create a list of lowercased names
#lowercased = ["YOUR CODE HERE!"]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [nn.title() for nn in lower_lc]
print(titlecased)

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
