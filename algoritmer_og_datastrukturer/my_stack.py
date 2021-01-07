def is_emmpty():
    if self.head == self.tail:
        return True
    else:
        return False

def is_full(self):
    if self.head - self.tail == 1:
        return True
    elif self.tail == len(self.array)-1 and self.head == 0:
        return True
    else:
        return False



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
