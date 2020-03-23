import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from math import sqrt

from random import randint

from Book_data import Book, Books_data

class Book_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.data = Books_data(False)

        self.build_GUI()

        self.opdater_tabel()

    def opdater_tabel(self):
        l = self.data.get_book_list(200)

        self.db_view.delete(*self.db_view.get_children())
        for b in l:
            self.db_view.insert("", tk.END, values=(b.titel, b.forfatter, b.aarstal, b.get_rating(), b.id))

    def on_book_selected(self, event):
        curItem = self.db_view.item(self.db_view.focus())['values']
        if len(curItem) > 0:
            b = self.data.get_book(curItem[4])

            self.lbl_titel.configure(text="Titel: {}".format(b.titel))
            self.lbl_forfatter.configure(text="Forfatter: {}".format(b.forfatter))

            self.can.delete("all")
            print(b.ratings[0]/sum(b.ratings))

            self.can.create_line(5,195,5,5, arrow=tk.LAST)
            self.can.create_line(5,195,165,195, arrow=tk.LAST)
            for i in range(0,len(b.ratings)):
                self.can.create_rectangle(i*25 + 10,190,i*25 + 30,190-200*(b.ratings[i]/sum(b.ratings)))


    def slet_bog(self):
        curItem = self.db_view.item(self.db_view.focus())['values']

        if len(curItem) > 0:
            b = Book()
            b.titel = curItem[0]
            b.forfatter = curItem[1]
            b.aarstal = curItem[2]
            b.id = int(curItem[4])

            self.data.slet_bog(b)
            self.opdater_tabel()


    def rediger_bog(self):
        def change_book():
            b.titel = en_titel.get()
            b.forfatter = en_forfatter.get()
            self.data.update_book(b)
            b.give_rating(sc_rating.scale.get())
            self.opdater_tabel()
            dlg.destroy()
            dlg.update()

        def close():
            dlg.destroy()
            dlg.update()

        curItem = self.db_view.item(self.db_view.focus())['values']

        if len(curItem) > 0:
            b = self.data.get_book(curItem[4])

            dlg = tk.Toplevel()

            lbl_titel = ttk.Label(dlg, text='Titel')
            lbl_titel.grid(column =0, row = 0)
            en_titel = ttk.Entry(dlg)
            en_titel.grid(column=1, row=0)
            en_titel.delete(0, tk.END)
            en_titel.insert(0, b.titel)

            lbl_forfatter = ttk.Label(dlg, text='Forfatter')
            lbl_forfatter.grid(column =0, row = 1)
            en_forfatter = ttk.Entry(dlg)
            en_forfatter.grid(column=1, row=1)
            en_forfatter.delete(0, tk.END)
            en_forfatter.insert(0, b.forfatter)

            lbl_rating = ttk.Label(dlg, text='Rating')
            lbl_rating.grid(column =0, row = 2)
            sc_rating = ttk.LabeledScale(dlg, from_ = 0, to = 5)
            sc_rating.value = b.get_rating()
            sc_rating.grid(column=1, row=2)

            but_annuller = ttk.Button(dlg, text="Annuller", command=close)
            but_annuller.grid(column=1,row=3)
            but_ok = ttk.Button(dlg, text="Gem ændringer", command=change_book)
            but_ok.grid(column=0,row=3)

    def sorterTitel(self):
        self.data.sorter("titel")
        self.opdater_tabel()

    def sorterForfatter(self):
        self.data.sorter("forfatter")
        self.opdater_tabel()

    def sorterAarstal(self):
        self.data.sorter("aarstal")
        self.opdater_tabel()

    def sorterRating(self):
        self.data.sorter("rating")
        self.opdater_tabel()

    def log_text(self, msg):
        self.cons.configure(state='normal')
        self.cons.insert(tk.END, msg + '\n')
        self.cons.configure(state='disabled')
        # Autoscroll to the bottom
        self.cons.yview(tk.END)

    def ansaet(self):
        #(Opgave 4)
        #Denne funktion skal ansætte en ny Employee i butikken
        self.data.ansaet()
        self.update_ui()

    def fyr(self):
        #(Opgave 4)
        #Denne funktion skal fyre en af de ansatte
        self.data.fyr()
        self.update_ui()

    def udbetal_loen(self):
        l = self.data.udbetal_loen()
        self.log_text("Der blev udbetalt {} i løn".format(l))
        self.update_ui()

        self.after(30000, self.udbetal_loen)

    def simulate_customer(self):
        #(Opgave 3)
        #Lav om så kunden køber for flere penge, hvis der er
        #flere ansatte. Eller lav din egen model, som du synes er sjov.

        #Udsalg?
        rabat = self.sc_tilbud.scale.get() * 0.01

        amount = int(rabat * randint(100,200) + randint(0,int(500*sqrt(len(self.data.ansatte)))))
        self.data.indtaegt(amount)

        self.log_text("En kunde købte for {}".format(amount))
        self.update_ui()

        #Hvis der er udsalg, kommer der hurtigere nye kunder!
        self.after(int(5000*rabat), self.simulate_customer)


    def update_ui(self):
        self.lblAnsatte.configure(text="Antal ansatte: {}".format(len(self.data.ansatte)))
        self.lblMoney.configure(text="Pengebeholdning: {}".format(self.data.money))


    def build_GUI(self):
        self.tabs = ttk.Notebook(self)
        bog_fane = ttk.Frame(self.tabs)
        sim_fane = ttk.Frame(self.tabs)

        self.tabs.add(bog_fane, text='Bøger')
        self.tabs.add(sim_fane, text='Simulering')

        right_frame = ttk.Frame(bog_fane)
        top_frame = ttk.Frame(right_frame)
        data_frame = ttk.Frame(right_frame)
        knap_frame = ttk.Frame(bog_fane)


        self.edit_button = ttk.Button(knap_frame, text="Rediger bog", command=self.rediger_bog)
        self.edit_button.pack(side=tk.TOP)

        self.del_button = ttk.Button(knap_frame, text="Slet bog", command=self.slet_bog)
        self.del_button.pack(side=tk.TOP)

        self.cons = ScrolledText(sim_fane, state='disabled', height=12)
        self.cons.pack(side = tk.TOP)
        self.cons.configure(font='TkFixedFont')
        self.after(1000, self.simulate_customer)

        butAnsaet = ttk.Button(sim_fane, text="Ansæt en person", command=self.ansaet)
        butAnsaet.pack(side=tk.TOP)
        butFyr = ttk.Button(sim_fane, text="Fyr en person", command=self.fyr)
        butFyr.pack(side=tk.TOP)
        self.after(3000, self.udbetal_loen)
        self.lblMoney = ttk.Label(sim_fane, text="Pengebeholdning: {}".format(self.data.money))
        self.lblMoney.pack(side=tk.TOP)
        self.lblAnsatte = ttk.Label(sim_fane, text="Antal ansatte: {}".format(len(self.data.ansatte)))
        self.lblAnsatte.pack(side=tk.TOP)
        self.sc_tilbud = ttk.LabeledScale (sim_fane,from_=50,to=110)
        self.sc_tilbud.pack(side=tk.TOP)

        self.db_view = ttk.Treeview(data_frame, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.on_book_selected)
        self.db_view.heading("#1", text="Titel", command=self.sorterTitel)
        self.db_view.heading("#2", text="Forfatter", command=self.sorterForfatter)
        self.db_view.heading("#3", text="Årstal", command=self.sorterAarstal)
        self.db_view.heading("#4", text="Rating", command=self.sorterRating)
        self.db_view.heading("#5", text="id")
        #Læg mærke til at kolonne 5 ikke bliver vist.
        #Vi kan stadig finde id på den bog der er valgt,
        #men brugeren kan ikke se id.
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(data_frame, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP, fill=tk.BOTH)

        #Top Frame
        self.can = tk.Canvas(top_frame, width=200, height=200)
        self.can.grid(column=1, row=0, rowspan=2)

        self.lbl_titel = ttk.Label(top_frame, text='Titel')
        self.lbl_forfatter = ttk.Label(top_frame, text='Forfatter')
        self.lbl_titel.grid(column=0, row=0)
        self.lbl_forfatter.grid(column=0, row=1)

        top_frame.pack(side=tk.TOP)
        data_frame.pack(side = tk.TOP)
        knap_frame.pack(side = tk.LEFT, fill=tk.Y)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabs.pack(expand=1, fill="both")

        self.pack()

root = tk.Tk()
root.geometry("800x600")

app = Book_gui(root)
app.master.title('Bøger')
app.mainloop()
