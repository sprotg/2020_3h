class ColorItem:
    def __init__(self):
        self.color = (0,0,0)
        self.x = 0
        self.y = 0
        self.size = 1

    def set_color(self, r, g, b):
        self.color = (r,g,b)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def grow(self, f):
        print(self.size)
        self.size *= f
        print(self.size)

    def shrink(self, f):
        self.size /= f

import tkinter as tk
import random
root = tk.Tk()

canvas = tk.Canvas(root,height=300, width=300)
canvas.pack()

items = [ColorItem() for i in range(10)]
for i in items:
    i.set_color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    i.set_pos(random.randint(0,300), random.randint(0,300))
    i.grow(20 + random.random()*20)
    canvas.create_oval(i.x, i.y, i.x + i.size, i.y + i.size, fill = "#%02x%02x%02x" % i.color)

root.mainloop()
