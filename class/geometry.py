import math
class Triangle():
    def __init__(self, a, b ,c ,h ):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def get_s(self):
        return 1/2 * self.a * self.h
    def get_p(self):
        return self.a + self.b + self.c

a = Triangle(5, 3, 4, 5)
print(a.get_s())
print(a.get_p())


class Circle():
    def __init__(self, d, r ):
        self.d = d
        self.r = r
    def get_l(self):
        return math.pi * self.d
    def get_pl(self):
        return math.pi * self.r ** 2

c = Circle(5, 3)
print(c.get_l())
print(c.get_pl())
