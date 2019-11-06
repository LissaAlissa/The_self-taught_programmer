class Apple():
    def __init__(self, w, c, v, l):
        self.weight = w
        self.color = c
        self.varienty = v
        self.location = l
        print("Яблоко")

my_apple = Apple(200, 'green', 'gloster', 'belarus')
print(my_apple.color)
print(my_apple.varienty)