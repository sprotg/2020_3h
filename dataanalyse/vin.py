import csv

def findMindsteAlkohol():
    min = 1000
    plads = 0

    for i in range(len(data)):
        vin = data[i]
        if float(vin['alcohol']) < min:
            min  = float(vin['alcohol'])
            plads = i

    return min, plads


#Her åbnes filen med data
infile = open('wineQualityReds.csv', mode='r')
#CSV-data læses
reader = csv.DictReader(infile)
#og konverteres til en liste:
data = list(reader)

cmd = ''

while cmd != 'q':
    cmd = input("Kommando: ")

    if cmd == 'header':
        print(reader.fieldnames)
    elif cmd == 'alkohol':
        #Lav analyse af alkohol
        min, plads = findMindsteAlkohol()
        print("Den vin med mindst alkohol har en alkoholprocent på {} og findes på plads {}.".format(min, plads))
