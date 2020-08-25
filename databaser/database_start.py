import sqlite3

#Her oprettes en forbindelse til databasefilen
#Hvis filen ikke findes, vil sqlite oprette en ny tom database.
con = sqlite3.connect('start.db')
print('Database åbnet')

try:
    con.execute("""CREATE TABLE personer (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		navn STRING,
        alder INTEGER)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

try:
    con.execute("""CREATE TABLE venner (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		person1 INTEGER,
        person2 INTEGER)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')


c = con.cursor()
#c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', ("Hans", 38))
#c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', ("Kim", 37))
#c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', ("Jesper", 37))

#Efter at have ændret i databasen skal man kalde funktionen commit.
con.commit()

#Denne variabel bruges til at modtage input fra brugeren
inp = ''

print('')
print('Kommandoer: ')
print('  vis - Viser alle personer i databasen')
print('  ny  - Opret ny person')
print('  ven  - Forbindelse mellem venner')
print('  venneliste - Vis venner')
print('  q   - Afslut program')

while not inp.startswith('q'):
    inp = input('> ')

    if inp == 'vis':
        c = con.cursor()
        c.execute('SELECT navn,alder FROM personer')

        for p in c:
            print('{} er {} år'.format(p[0], p[1]))

    elif inp == 'ny':
        n = input('Indtast navn: ')
        a = input('Indtast alder: ')
        c = con.cursor()
        c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', (n, a))
        con.commit()


    elif inp == 'ven':
        c = con.cursor()
        c.execute("SELECT id, navn FROM personer;")

        for p in c:
            print("{}: {}".format(p[0],p[1]))
        n1 = input("Vælg første person: ")
        n2 = input("Vælg anden person: ")
        c.execute("INSERT INTO venner (person1, person2) VALUES (?,?)",[n1,n2])
        con.commit()

    elif inp == 'venneliste':
        c = con.cursor()
        c.execute("SELECT navn FROM personer;")

        for p in c:
            print("{}".format(p[0]))
        n = input("Vælg person: ")
        c.execute("SELECT p1.navn, p2.navn FROM venner JOIN personer p1 ON venner.person1 = p1.id JOIN personer p2 on venner.person2 = p2.id WHERE p1.navn = ?",[n])
        for ven in c:
            print("{} er ven med {}".format(ven[0],ven[1]))
