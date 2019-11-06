class Shape():
    def __init__(self, w, l):
        self.widht = w
        self.len = l
    
    def print_size(self):
        print('''{} на {}'''.format(self.widht, self.len))

class Square(Shape):
    def area(self):
        return self.widht * self.len

    def print_size(self):
        print('''Я {} на {}'''.format(self.widht, self.len))


a_square = Square(20, 20)
a_square.print_size()