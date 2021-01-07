from random import randint

class Heap():

    def __init__(self):
        self.a = [randint(1,100) for i in range(10)]
        self.heap_size = len(self.a)

    def left(self, i):
        return 2*i + 1


    def right(self, i):
        return 2*i + 2

    def parent(self, i):
        return (i-1)//2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.a[l] > self.a[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.a[r] > self.a[largest]:
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = len(self.a)
        for i in reversed(range(len(self.a))):
            self.max_heapify(i)

    def heapsort(self):
        pass
        
h = Heap()
print(h.a)
h.build_max_heap()
print(h.a)
