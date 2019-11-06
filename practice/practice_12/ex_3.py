class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.hight = h

    def area(self):
        return self.base * 0.5 * self.hight

triangle = Triangle(3, 4)
print(triangle.area())