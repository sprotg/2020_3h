class My_stack():
    def __init__(self):
        self.array = [0 for i in range(10)]
        self.top = -1

    def push(self, x):
        self.top += 1
        self.array[self.top] = x

    def pop(self):
        if self.is_empty():
            raise Exception("Kan ikke pop'e fra en tom stack")
        else:
            self.top -= 1
            return self.array[self.top + 1]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

stack = My_stack()
stack.push(5)
stack.pop()
stack.pop()
