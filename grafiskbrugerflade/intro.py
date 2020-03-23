import tkinter as tk
from tkinter import ttk

#https://effbot.org/tkinterbook/tkinter-index.htm

def klik():
    t = float(e.get())
    l.configure(text=t/7.47)
    can.create_rectangle(50, 25, 150, 75, fill="blue")


main = tk.Frame()

main.pack()

V =
ame(H)

H.pack(side=tk.RIGHT)
V.pack(side=tk.RIGHT)

HT.pack(side=tk.TOP)
HB.pack(side=tk.TOP)

b = tk.Button(V, text  = "Klik her", command=klik)
b.pack(side = tk.TOP, fill = tk.BOTH)

e = tk.Entry(V, text="tekst")
e.pack(side=tk.TOP, fill =tk.BOTH)


l = tk.Label(HT, text="her står noget")
l.pack(side=tk.LEFT, fill = tk.BOTH)
l2 = tk.Label(HT, text="her står noget andet")
l2.pack(side=tk.LEFT, fill = tk.BOTH)

can = tk.Canvas(HB)
can.pack()


main.mainloop()
