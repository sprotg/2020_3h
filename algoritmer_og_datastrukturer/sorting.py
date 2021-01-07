from random import randint
import time
import matplotlib.pyplot as plt

antal = []
tid = []

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = 100
for n in range(1000,20000,1000):
    a = [randint(0,100) for i in range(n)]

    starttid = time.time()

    bubbleSort(a)

    sluttid = time.time()
    total = sluttid - starttid
    antal.append(n)
    tid.append(total)

plt.plot(antal,tid)
plt.show()
