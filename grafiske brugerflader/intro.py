import tkinter as tk

def klik():
    t = e.get()
    l.configure(text=t)


main = tk.Frame()

b = tk.Button(main, text  = "Klik her", command=klik)
b.pack(side = tk.LEFT, fill = tk.BOTH)

e = tk.Entry(main, text="tekst")
e.pack(side=tk.LEFT, fill =tk.BOTH)

l = tk.Label(main, text="her står noget")
l.pack(side=tk.LEFT, fill = tk.BOTH)



main.pack()

main.mainloop()
