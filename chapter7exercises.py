import random

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in shows:
    print(show)

for i in range(25, 51):
    print(i)

idx = 0
for i, show in enumerate(shows):
    print(shows[i])
    print(i)
    i += 1

def guesser(guess):
    r = random.randint(0,9)
    r = str(r)
    g = guess
    if g == r:
        return True
    else:
        return False

while True:
    guess = input("Guess a number between 0 and 9. Type 'q' to quit")
    if guess == "q":
        break
    else:
        response = guesser(guess)
        if response == True:
            print("You Guessed Correctly!")
        else:
            print("Sorry, that was not correct!")

l1 = [8, 19, 148, 4]
l2 = [9, 1, 33, 83]
l3 = []
for i in l1:
    for j in l2:
        result = i + j
        l3.append(result)
print(l3)
        

