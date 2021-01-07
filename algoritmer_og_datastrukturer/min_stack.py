class My_stack:
    def __init__(self):
        self.top = -1
        self.array = [0 for i in range(10)]

    def stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, x):
        self.top += 1
        self.array[self.top] = x

    def pop(self):
        if self.stack_empty():
            raise IndexError('list index out of range')
        else:
            self.top -= 1
            return self.array[self.top + 1]

    def __str__(self):
        return str(self.array) + " " + str(self.top)

my_stack = My_stack()

my_stack.push(5)
print(my_stack)
my_stack.push(2)
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.push(7)
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
