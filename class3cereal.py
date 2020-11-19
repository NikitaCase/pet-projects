import os
import csv

# filepath = os.path.join("cereal.csv", "r")
with open("cereal.csv", "r") as file:
    cereals = csv.reader(file)

    header = next(file)

    for cereal in cereals:
        if float(cereal[7]) >= 5:
            print(cereal)


