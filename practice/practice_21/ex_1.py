class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self, items):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

stack = Stack()

for c in "позавчера":
    stack.push(c)

revers = ''

for i in range(len(stack.items)):
    revers += stack.pop()

print(revers)