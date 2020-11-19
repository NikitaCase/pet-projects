

for n in [1,2,3,4,5]:
    print(n)

for p in range(5):
    print(p)

for q in range(1,5):  # will cut off your last value
    print(q)

word = "antidisestablishmentarianism"
for l in word:
    print(l)

zoo = ["panda","koala","polar bear"]
for animal in zoo:
    print(animal)

# now for a wile loop
run = "y"

# if you set while to true then it is infinite
while run == "y":
    print("run! run! run! running!")
    run = (input("continue running? press 'y'"))

