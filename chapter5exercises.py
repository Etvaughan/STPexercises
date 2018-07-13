myMusic = ["Gunship", "Coheed and Cambria", "Timecop1983", "Chance the Rapper", "Lorde"]
print(myMusic)



myLocations = [(40.8021, -124.1637),
               (32.157, -117.1611),
               (34.0522, -118.2437)]
print(myLocations)



myStats = {"height":"5'9", "color":"Navy", "author":"Neil Gaiman"}
print(myStats)

def asker():
    n = input("What do you want to know?")
    if n in myStats:
        print(myStats[n])

    else:
        print("I don't know the answer to that")

asker()



faveSongs = {"Chance the Rapper":
             ["Same Drugs", "Slow Jam",
              "Summer Friends", "Finish Line"],

             "Guneship":
             ["Tech Noir", "The Mountain",
              "Kitsune"],

             "Lorde":
             ["Louvre", "Liability",
              "Homemade Dynamite",
              "Green Light"]}

def musicAsk():
    n = input("Which artist do you want?")
    if n in faveSongs:
        print(faveSongs[n])

    else:
        print("That's not one of my favorite artists!")

musicAsk()






