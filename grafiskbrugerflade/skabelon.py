import tkinter as tk
from random import randint

class Min_gui(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.build_GUI()

    def change(self):
        self.c.create_rectangle(50, 25, 150, 75, fill="blue")


    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.V = tk.Frame(self)
        self.H = tk.Frame(self)
        self.HT = tk.Frame(self.H)
        self.HB = tk.Frame(self.H)

        self.V.pack(side = tk.LEFT)
        self.H.pack(side = tk.RIGHT, fill = tk.X)
        self.HT.pack(side = tk.TOP)
        self.HB.pack(side = tk.BOTTOM)

        for i in range(4):
            b = tk.Button(self.V, text = "{}".format(randint(50,500)), command=self.change)
            b.pack(side = tk.TOP, fill = tk.BOTH)
        for i in range(2):
            b = tk.Button(self.HT, text = "{}".format(randint(50,500)), command=self.change)
            b.pack(side = tk.LEFT)
        self.c = tk.Canvas(self.HB, width=200, height=100)
        self.c.pack(side = tk.TOP, fill = tk.BOTH)


app = Min_gui()

app.mainloop()
