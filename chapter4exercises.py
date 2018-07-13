def squareMe(x):
    """
    Returns x squared.
    param x: int.
    """
    return x*x

c1 = squareMe(2)
print(c1)

def stringPrint(stringIn):
    """
    Prints the string that is passed as a parameter.
    param stringIn: str.
    Prints "(stringIn)".
    """
    print(stringIn)

stringPrint("This is challenge 2")

def fiveAdd(j, k, x=2, y=3, z=4):
    """
    Returns 5 integers added together.
    param j: int.
    param k: int.
    param x: int. defaults to 2.
    param y: int. defaults to 3.
    param z: int. defaults to 4.
    """
    intSum = j+k+x+y+z
    return intSum

c3 = fiveAdd(10, 5)
print(c3)

def f1(x):
    """
    Returns x divided by 2.
    param x: int.
    """
    return x / 2

def f2(y):
    """
    Returns y multiplied by 4.
    param y: int.
    """
    return y * 4

v1 = f1(8)
c4 = f2(v1)
print(c4)

def floatConvert(fInput):
    """
    Returns the input converted to a float.
    param fInput: string.
    Returns float(fInput)
    """
    try:
        return float(fInput)
    except ValueError:
        print("This string is not a number that can be converted")

c5 = floatConvert("prince")
print (c5)

