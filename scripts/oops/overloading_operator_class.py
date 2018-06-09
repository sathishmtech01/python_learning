# OOPS Learnings
"""
1. Overloading Operator

"""

class Vector:
    print("Vector")
    # constructor
    # variable initialiation
    def __init__(self, a, b):
        # print("Init Method")
        # print(a)
        # print(b)
        self.a = a
        self.b = b

    # Constructor
    # for string operation return only string values
    def __str__(self):
        # print("String Constuctor")
        # print(type(self.a))
        return 'Vector (%d, %d)' % (self.a, self.b)

    # Constructor
    # for add operation
    def __add__(self, other):
        print("add")
        print(self)
        print(other)
        print("add")
        return Vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        print("sub")
        return Vector(self.a - other.a, self.b - other.b)

if __name__ == '__main__':

    v1 = Vector(2, 10)
    print(type(v1))

    v2 = Vector(5, -2)

    v3 = Vector(6, 6)
    #print(v2)
    print(v1+v2+v3)
    #print(v1 - v2)

    input()

    v2 = Vector(5, -2)
    v3 = Vector(6,6)
    print(v1+v2+v3)
