import random
from jinja2 import Template
import os
from math import cos, sin, atan2, pi

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg7_template.svg')) as f:
    tmpl = Template(f.read())

## Opgave:
# 1. Lad os genskabe logoet fra "Startup academy"
# Se slide 5 på https://docs.google.com/presentation/d/1FBLW7up4vCegVcO-lprlE2hdwNsjwgYpJzmFWOy6eMg/edit?usp=sharing

#først skal vi bruge punkterne i en 7-kant:
syvkant = ""
radius = 50 # pixels
for n in range(7):
    vinkel = n*2*pi/7

    syvkant = syvkant + "{},{} ".format(radius*cos(vinkel),radius*sin(vinkel))

print(syvkant)
sx = random.randint(-20,20)
sy = random.randint(-20,20)

r1 = random.randint(0,255)
g1 = random.randint(0,255)
b1 = random.randint(0,255)

r2 = random.randint(0,255)
g2 = random.randint(0,255)
b2 = random.randint(0,255)

vinkel = random.randint(0,360)

#TODO:
# Lav en kopi af syvkanten og fyld den med en farve
# Tilføj en gradient som farve.
# Generer de to farver i gradienten tilfældigt med hsv eller vælg fra en liste med udvalgte farver.
# Lav en transformation af den farvede syvkant. F.eks. med skewX() og skewY(): https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#skewx
# Tilføj tekst?

#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg7.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render(syvkant=syvkant, sx=sx, sy=sy, r1=r1, g1=g1, b1=b1, r2=r2, g2=g2, b2=b2, vinkel=vinkel))
output_svg.close()
