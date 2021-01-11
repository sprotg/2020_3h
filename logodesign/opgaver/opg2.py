import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg2_template.svg')) as f:
    tmpl = Template(f.read())


## Opgave:
# 1. Filen opg2_template.svg viser en simpel firkant, lavet som en polygon
# 2. Få programmet til at generere en tilfældig farve til polygonen hver gang programmet kører
# 3. Lav om i polygonen ved at skrive nogle andre eller nogle flere koordinater i svg-filen.
# 4. Få desuden programmet til at gentage polygonen flere gange vha. en for-løkke.



#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg2.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render())
output_svg.close()
