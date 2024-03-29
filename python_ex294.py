class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
for c in "Привет":
    stack.push(c)

revers = ''

for i in range(len(stack.items)):
    revers += stack.pop()

print(revers)
