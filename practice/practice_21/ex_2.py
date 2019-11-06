class Stack:
    def __init__(self):
        self.items = []

    def  is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return len(self.items) - 1

    def size(self):
        return len(self.items)

stack = Stack()
for c in range(0, 6):
    stack.push(c)

reverse = ''

for i in range(len(stack.items)):
    reverse += str(stack.pop())

print(reverse)