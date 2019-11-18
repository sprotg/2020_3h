import csv

#Her åbnes filen med data
infile = open('pizzaer.csv', mode='r')
#CSV-data læses
reader = csv.DictReader(infile)
#og konverteres til en liste:
data = list(reader)


for p in data:
    if p['navn'] == 'hawaii':
        print(p['navn'])
