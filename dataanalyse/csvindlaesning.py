import csv
import matplotlib.pyplot as plt
from math import sqrt

def findMaxAlkohol():
    min = 0
    for i in range(len(data)):
        row = data[i]
        alc = float(row['alcohol'])
        if alc > min:
            min = alc
            plads = i
    #Funktionen returnerer både den største værdi
    #og den plads hvor den blev fundet.
    return min,plads

def findMindsteAlkohol():
    min = 100
    for i in range(len(data)):
        row = data[i]
        alc = float(row['alcohol'])
        if alc < min:
            min = alc
            plads = i
    #Funktionen returnerer både den mindste værdi
    #og den plads hvor den blev fundet.
    return min,plads


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
        min,plads = findMindsteAlkohol()
        print("Den vin med mindst alkohol er på plads {} og har en alkoholprocent på {}".format(plads,min))
        max,plads = findMaxAlkohol()
        print("Den vin med mest alkohol er på plads {} og har en alkoholprocent på {}".format(plads,max))

        #Visualisering i histogram
        #Først laves en liste af alkoholværdier
        liste = []
        for row in data:
            liste.append(row['alcohol'])
        #Antallet af bins i vores histogram:
        b = int(sqrt(len(liste)))

        plt.hist(liste, b)
        plt.show()
