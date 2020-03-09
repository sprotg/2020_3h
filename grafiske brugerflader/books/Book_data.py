import csv

class Book:

    def __init__(self):
        self.titel = ""
        self.forfatter = ""
        self.aarstal = 0
        #[1 stjerne, 2 stjerner, 3 stjerner...]
        self.ratings = [0,0,0,0,0]
        self.id = -1

    def get_rating(self):
        r = 0
        total = 0
        for i in range(0,len(self.ratings)):
            r += (i+1)*self.ratings[i]

        return r/sum(self.ratings)

    def give_rating(self, r):
        if 0 <= r <= 5:
            self.ratings[int(r)-1] += 1
        else:
            print("Fejl, rating er ikke gyldig")


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
                b.ratings[0] = int(book["ratings_1"])
                b.ratings[1] = int(book["ratings_2"])
                b.ratings[2] = int(book["ratings_3"])
                b.ratings[3] = int(book["ratings_4"])
                b.ratings[4] = int(book["ratings_5"])
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
        '''
        Slet en bog med et bestemt id
        '''
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
                book.aarstal = b.aarstal
