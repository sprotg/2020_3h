import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg2_template.svg')) as f:
    tmpl = Template(f.read())


## Opgave:
# 1. Filen opg2_template.svg viser en simpel firkant.
# 2. Få programmet til at generere en tilfældig farve til firkanten hver gang programmet kører



#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg2.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render())
output_svg.close()
