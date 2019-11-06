from ex_3 import Shape

class Rectangle(Shape):
    def __init__(self, w, l):
        self.widht = w
        self.len = l

    def calulate_perimeter(self):
        return self.widht * 2 + self.len * 2

class Square(Shape):
    def __init__(self, w):
        self.widht = w

    def change_size(self, n):
        self.widht += n

    def calculate_perimeter(self):
        return self.widht * 4
        


my_rectangle = Rectangle(2, 6)
print(my_rectangle.calulate_perimeter())
my_rectangle.what_am_i()

my_square = Square(3)
print(my_square.calculate_perimeter())
my_square.change_size(- 2)
print(my_square.calculate_perimeter())
my_square.what_am_i()