import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg1_template.svg')) as f:
    tmpl = Template(f.read())


## Opgave:
# 1. Lav en svg-fil med en simpel firkant.
# 2. Få python programmet til at generere tre tilfældige tal mellem 0 og 255.
# 3. Send farven til skabelonen, så firkanten får en tilfældig farve hver gang.


#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg1.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render())
output_svg.close()
