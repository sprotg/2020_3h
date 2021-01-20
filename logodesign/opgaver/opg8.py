import random
from jinja2 import Template
import os
from math import cos, sin, atan2, pi

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg8_template.svg')) as f:
    tmpl = Template(f.read())

## Opgave:
# 1.
pinde = ["pind1", "pind2", "pind3"]
#OTGblue {RGB}{0,141,156}
#OTGgreen {RGB}{212,209,72}
#OTGgray {RGB}{152,153,157}
farver = ["0,141,156", "212,209,72", "152,153,157"]

random.shuffle(farver)
random.shuffle(pinde)

#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg8.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render(pinde=pinde, farver=farver))
output_svg.close()
