import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from math import sin, pi
import csv
import imageio
import datetime

def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)


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
        n = 0
        for row in data:
            if row['Uddannelse'] == 'HTX':
                for key, value in list(row.items())[1:]:
                    sum += int(value)
                    n = n + 1
                print("I 2012-2018 gik der i gennemsnit {} elever på HTX.".format(sum/n))

    elif cmd == 'plot':
        #Animation:
        #https://www.idiotinside.com/2017/06/06/create-gif-animation-with-python/

        #https://www.reddit.com/r/dataisbeautiful/comments/dsv88h/how_did_the_uks_regions_respond_to_the_2008_house/
        fig, ax = plt.subplots()
        for row in data:
            if row['Uddannelse'] == 'HTX':
                for n in range(1,8):
                    tal = []
                    aar = []
                    for key, value in list(row.items())[1:]:
                        if int(key) < int('2012') + n:
                            tal.append(int(value))
                        else:
                            tal.append(0)
                        aar.append(key)
                    ax.set_ylim(0,15000)
                    ax.bar(aar, tal, color='green')
                    plt.savefig('{}.png'.format(n))
                create_gif(['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png'], 1)


    elif cmd == 'kunst':
        ellipser = []
        for x in range(20):
            for y in range(20):
                vinkel = sin(0.1*x*y)*360/(2*pi)
                ellipser.append(Ellipse([x, y], 1, 0.6, angle=vinkel))

        fig, ax = plt.subplots()

        for e in ellipser:
            ax.add_artist(e)

        ax.set_xlim(-1, 21)
        ax.set_ylim(-1, 21)
        ax.set_frame_on(False)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
