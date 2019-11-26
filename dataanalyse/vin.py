import csv
import matplotlib.pyplot as plt

def findMaxAlkohol():
    max = 0
    plads = 0

    for i in range(len(data)):
        vin = data[i]
        if float(vin['alcohol']) > max:
            max  = float(vin['alcohol'])
            plads = i

    return max, plads

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
        max, plads = findMaxAlkohol()
        print("Den vin med mest alkohol har en alkoholprocent på {} og findes på plads {}.".format(max, plads))

        liste = []
        for vin in data:
            liste.append(vin['alcohol'])

        plt.hist(liste, bins = 7)
        plt.show()
