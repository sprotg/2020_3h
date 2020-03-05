import tkinter as tk
import tkinter.ttk as ttk
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
            self.db_view.insert("", tk.END, values=(b.titel, b.forfatter, b.aarstal, b.rating, b.id))

    def on_book_selected(self, event):
        curItem = self.db_view.item(self.db_view.focus())['values']
        if len(curItem) > 0:
            print(curItem)


    def slet_bog(self):
        curItem = self.db_view.item(self.db_view.focus())['values']

        if len(curItem) > 0:
            b = Book()
            b.titel = curItem[0]
            b.forfatter = curItem[1]
            b.aarstal = curItem[2]
            b.rating = curItem[3]
            b.id = int(curItem[4])

            self.data.slet_bog(b)
            self.opdater_tabel()


    def rediger_bog(self):
        def change_book():
            b.titel = en_titel.get()
            b.forfatter = en_forfatter.get()
            b.rating = sc_rating.scale.get()
            self.data.update_book(b)
            self.opdater_tabel()
            dlg.destroy()
            dlg.update()

        def close():
            dlg.destroy()
            dlg.update()

        curItem = self.db_view.item(self.db_view.focus())['values']

        if len(curItem) > 0:
            b = Book()
            b.titel = curItem[0]
            b.forfatter = curItem[1]
            b.aarstal = curItem[2]
            b.rating = curItem[3]
            b.id = int(curItem[4])

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
            sc_rating.value = b.rating
            sc_rating.grid(column=1, row=2)

            but_annuller = ttk.Button(dlg, text="Annuller", command=close)
            but_annuller.grid(column=1,row=3)
            but_ok = ttk.Button(dlg, text="Gem ændringer", command=change_book)
            but_ok.grid(column=0,row=3)



    def build_GUI(self):
        right_frame = ttk.Frame(self)
        top_frame = ttk.Frame(right_frame)
        data_frame = ttk.Frame(right_frame)
        knap_frame = ttk.Frame(self)

        self.edit_button = ttk.Button(knap_frame, text="Rediger bog", command=self.rediger_bog)
        self.edit_button.pack(side=tk.TOP)

        self.del_button = ttk.Button(knap_frame, text="Slet bog", command=self.slet_bog)
        self.del_button.pack(side=tk.TOP)

        self.db_view = ttk.Treeview(data_frame, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.on_book_selected)
        self.db_view.heading("#1", text="Titel")
        self.db_view.heading("#2", text="Forfatter")
        self.db_view.heading("#3", text="Årstal")
        self.db_view.heading("#4", text="Rating")
        self.db_view.heading("#5", text="id")
        #Læg mærke til at kolonne 5 ikke bliver vist.
        #Vi kan stadig finde id på den bog der er valgt,
        #men brugeren kan ikke se id.
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(data_frame, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP, fill=tk.BOTH)

        top_frame.pack(side=tk.TOP)
        data_frame.pack(side = tk.TOP)
        knap_frame.pack(side = tk.LEFT, fill=tk.Y)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.pack()

root = tk.Tk()
root.geometry("800x600")

app = Book_gui(root)
app.master.title('Bøger')
app.mainloop()
