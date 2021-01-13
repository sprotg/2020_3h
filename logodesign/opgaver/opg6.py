import random
from jinja2 import Template
import os
from math import cos, sin, atan2

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg6_template.svg')) as f:
    tmpl = Template(f.read())

## Opgave:
# 1.
n=30
points = []
for i in range(n):
    direction = float(random.randint(0,628))/100
    ddir = float(random.randint(0,628))/100
    c1x = cos(direction + ddir) * random.randint(100,500)
    c1y = sin(direction + ddir) * random.randint(100,500)
    c2x = cos(direction) * random.randint(130,180)
    c2y = sin(direction) * random.randint(130,180)
    points.append([c1x,c1y,c2x,c2y])

#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg6.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render(n=n, points=points))
output_svg.close()
