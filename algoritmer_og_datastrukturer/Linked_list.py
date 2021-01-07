class DLList():

    def __init__(self, head):
        self.head = head

    def insert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    def print_list(self):
        e = self.head
        print("***")
        print(e.key)
        while e.next != None:
            e = e.next
            print(e.key)


class DLElem():

    def __init__(self, key):
        self.prev = None
        self.next = None
        self.key = key
if __name__ == "__main__":
    e1 = DLElem([100,140,10])
    liste = DLList(e1)
    liste.print_list()

    e2 = DLElem("Elem2")
    liste.insert(e2)
    liste.print_list()

    e3 = DLElem("Elem3")
    liste.insert(e3)
    liste.print_list()

    liste.delete(e2)
    liste.print_list()
