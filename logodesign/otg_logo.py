import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'otg_logo_1.svg')) as f:
    tmpl = Template(f.read())

heights = [random.randint(1,3) for _ in range(3)]


#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'otg_logo_1_result.svg'), "w")
n = output_svg.write(tmpl.render(heights = heights))
output_svg.close()
