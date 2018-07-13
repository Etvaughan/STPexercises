class Square():
    squares = []

    def __init__(self, side):
        self.side = side
        self.squares.append(side)

    def __repr__(self):
        ss = str(self.side)
        return ss+" by "+ss+" by "+ss+" by "+ss+"."


def same_checker(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False

def same_printer(status):
    if status is True:
        print("This is true!")
    else:
        print("This is False!")


s1 = Square(5)
s2 = Square(10)
s3 = Square(7)

print(s1)
print(s3)

s4 = s1

stat1 = same_checker(s1, s3)
same_printer(stat1)
stat2 = same_checker(s1, s4)
same_printer(stat2)

