class Shape:
        def getArea(self):
            pass

class Rectangle(Shape):
        def __init__(self, l, w):
                Shape.__init__("Rectangle")
                self.l = l
                self.w = w
        def getArea(self):
                return self.l * self.w
        
class Circle(Shape):
        def __init__(self, r):
                Shape.__init__("Circle")
                self.r = r
        def getArea(self):
                return 3.1415 * (self.r ** 2)

class Triangle(Shape):
        def __init__(self, b, h):
                Shape.__init__("Triangle")
                self.b = b
                self.h = h
        def getArea(self):
                return (self.b * self.h) / 2

with open("C:\DevSource\Kubitz_GEOG676\lab\week03\shapes.txt", "r") as file:
        for line in file:
            pieces = line.strip().split(",")
            shape_type = pieces[0]
            if shape_type == "Rectangle":
                    l, w = map(int, pieces[1:])
                    shape_instance = Rectangle(l, w)
            elif shape_type == "Circle":
                    r = int(pieces[1])
                    shape_instance = Circle(r)
            elif shape_type == "Triangle":
                    b, h = map(int, pieces[1:])
                    shape_instance = Triangle(b, h)
            else:
                    print("Unknown shape.")
                    continue

            area = shape_instance.getArea()
            print(area)