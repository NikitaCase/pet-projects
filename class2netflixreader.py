import csv

with open("netflix.csv","r") as file:
    ratings = csv.reader(file)

    movie = str(input("what is the movie name"))

    found = True

    for row in ratings:
        if movie == row[0]:
            print(row)
            break
        else:
            found = False

if found is False:
    print("movie not found")






    #for movie in ratings:
     #   print(movie)
      #  break
