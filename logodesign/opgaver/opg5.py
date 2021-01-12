import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg5_template.svg')) as f:
    tmpl = Template(f.read())

## Opgave:
# 1. I svg-filen er der lavet en "polyline". Kan du få programmet til at generere en liste af tilfældige punkter, og tegne en polyline mellem punkterne?
# 2. Prøv at sortere punkterne efter x-koordinat inden de sendes til svg-filen. Så burde du få en polyline uden nogle linjer der overlapper.

#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg5.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render())
output_svg.close()
