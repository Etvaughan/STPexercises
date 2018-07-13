class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)

    def what_am_i(self):
        print("I am a shape!")


class Square(Shape):

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)

    def change_size(self, i):
        self.width -= i
        self.length -= i


class Rectangle(Shape):

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)


square = Square(5, 5)
rect = Rectangle(5, 7)

square.what_am_i()
print(square.calculate_perimeter())
rect.what_am_i()
print(rect.calculate_perimeter())


class Rider():
    def __init__(self, n, g, c):
        self.name = n
        self.gender = g
        self.country = c


class Horse():
    def __init__(self, n, c, r):
        self.name = n
        self.color = c
        self.rider = r

r1 = Rider("Arnesto", "Male", "Bolivia")

h1 = Horse("Buttercup", "Brown", r1)

print(h1.name+"'s rider's name is "+h1.rider.name)
