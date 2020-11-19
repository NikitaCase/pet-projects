
mylist = ["jocab", 45, 2.56, True] #list is a data type, accepts all types
print(len(mylist))                  # lists are mutabe - changeable

print(mylist[2])

mylist.append("mana")
print(mylist)

mylist.remove(45)
print(mylist)

mylist.pop(0)
print(mylist)

mylist2 = [3,6,2,7,8,3,2,1]
mylist2.sort()
print(mylist2)

mylist2.sort(reverse=True)
print(mylist2)

mytuple = ("john", "jason", "shmit") # this is a tuple cannot change