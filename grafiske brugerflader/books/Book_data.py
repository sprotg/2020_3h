import csv

class Book:

    def __init__(self):
        self.titel = ""
        self.forfatter = ""
        self.aarstal = 0
        self.rating = 0
        self.id = -1

bog = Book()
print(bog.forfatter)


class Books_data:

    def __init__(self, samples = False):
        '''
        Variablen samples bestemmer om alle bøger skal indlæses,
        eller kun en lille del.
        '''
        if samples:
            infile = open('data\\samples\\books.csv', mode='r', encoding="utf8")
        else:
            infile = open('data\\books.csv', mode='r', encoding="utf8")
        reader = csv.DictReader(infile)

        self.books = []
        for book in reader:
            b = Book()
            try:
                b.titel = book["title"]
                b.rating = float(book["average_rating"])
                b.aarstal = book["original_publication_year"]
                b.forfatter = book["authors"]
                b.id = int(book['book_id'])
            except:
                print(book)

            self.books.append(b)
        print("Indlæst {} bøger".format(len(self.books)))

    def get_book_list(self, n=0):
        '''
        Returnerer en liste med n bøger.
        '''
        if n > 0:
            n = min(n, len(self.books)-1)
        else:
            n = len(self.books)-1
        return self.books[0:n]

    def slet_bog(self, b):
        for book in self.books:
            if book.id == b.id:
                self.books.remove(book)

    def get_book(self, id):
        '''
        find en bog med et bestemt id
        '''
        book = None
        for b in self.books:
            if b.id == id:
                book = b
        return book

    def update_book(self, b):
        '''
        Opdater oplysningerne om en bog
        '''
        for book in self.books:
            if book.id == b.id:
                book.forfatter = b.forfatter
                book.titel = b.titel
                book.rating = b.rating
                book.aarstal = b.aarstal
