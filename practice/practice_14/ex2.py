class Square():
    def __init__(self, w):
        self.w = w

    def print_size(self):
        print('''{} на {} на {} на {}'''.format(self.w, self.w, self.w, self.w))

s1 = Square(3)
s1.print_size()