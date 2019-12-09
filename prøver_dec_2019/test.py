import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from math import sin, pi
import csv

infile = open('gym-tal.csv', mode='r')
reader = csv.DictReader(infile)
data = list(reader)

cmd = ''


while not cmd.startswith('q'):
    cmd = input('Skriv en kommando > ')

    if cmd.startswith('header'):
        print(reader.fieldnames)
    elif cmd == 'gym':
        værdier = []
        labels = []
        for row in data:
            if row['Uddannelse'] == 'HTX':
                for år, antal in list(row.items())[1:]:
                    værdier.append(int(antal))
                    labels.append(år)
        plt.bar(labels, værdier)
        plt.show()

    elif cmd == 'gennemsnit':
        sum = 0
        n : 0
        for row in Data:
            if row['Uddanelse'] == 'HTX':
                for key, value in list(row.items())[1:]:
                    sum += value
                    n = n + 1
                print("I 2012-2018 gik der i gennemsnit {} elever på HTX.".format(sum/n))

    elif cmd == 'kunst':
        ellipser = []
        for x in range(10):
            for y in range(10):
                vinkel = sin(0.1*x*y)*360/(2*pi)
                ellipser.append(Ellipse([x, y], 1, 0.6, angle=vinkel))

        fig, ax = plt.subplots()

        for e in ellipser:
            ax.add_artist(e)

        ax.set_xlim(-1, 11)
        ax.set_ylim(-1, 11)
        ax.set_frame_on(False)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
