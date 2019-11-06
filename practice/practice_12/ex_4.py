class Hexagon():
    def __init__(self, l):
        self.len = l

    def calculator_perimeter(self):
        return self.len * 6

my_hexagon = Hexagon(6)
print(my_hexagon.calculator_perimeter())