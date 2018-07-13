s = "Camus"
print (s[0])
print (s[1])
print (s[2])
print (s[3])
print (s[4])


def twoString():
    n1 = input("choose story, song, poem, or report")
    n2 = input("choose friend, coworker, family member, or lover")
    print("Yesterday I wrote a "+n1+". I sent it to a "+n2+"!")

twoString()

s2 = "aldous Huxley was born in 1894."

print(s2.capitalize())

s3 = "Where now? Who now? When now?"
list3 = s3.split(" ")
list3 = [list3[0]+" "+list3[1],
         list3[2]+" "+list3[3],
         list3[4]+" "+list3[5]]
print(list3)

foxList = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(foxList)
fox = fox[:-2]
fox = fox+"."
print(fox)

scream = "A screaming comes across the sky"
scream = scream.replace("s", "$")
print(scream)

hem = "Hemingway"
idx = hem.index("m")
print(idx)

quoteString = "John said \"I can't do this anymore Joanna\"."
print(quoteString)

th = "three"
th1 = th+" "+th+" "+th
th2 = th*3
th2 = th2[:5]+" "+th2[5:10]+" "+th2[10:]
print(th1)
print(th2)


april = "It was a bright cold day in April, and the clocks were striking thirteen."
comma = april.index(",")
april = april[:comma]
print(april)

