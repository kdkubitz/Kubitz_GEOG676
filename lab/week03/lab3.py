class Rectangle(Shape):
        def __init__(self, l, w):
                self.l = l
                self.w = w
        def getArea(self):
                return self.l * self.w
        
class Circle(Shape):
        def __init__(self, r):
                self.r = r
        def getArea(self):
                return 3.1415 * (self.r ** 2)

class Triangle(Shape):
        def __init__(self, b, h):
                self.b = b
                self.h = h
        def getArea(self):
                return (self.b * self.h) / 2

  