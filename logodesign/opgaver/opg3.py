import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg3_template.svg')) as f:
    tmpl = Template(f.read())

n=5
## Opgave:
# 1. I svg-filen kan du se hvordan den grønne figur er dannet som et objekt med svg-kommandoen "g". Det der står under <defs> bliver ikke tegnet i sig selv, men kan bruges som et objekt senere i filen. Der tegnes først to figurer, og dernæst en række figurer vha. en for-løkke i jinja. Kan du tilføje et sort omrids om den grønne figur?
# 2. I jinja-løkken bliver hver grønne figur udsat for en transformation. Her kan du se nogle sjove eksempler på transformationer: https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform
# 3. Kan du få den grønne figur til at blive mindre og mindre, hver gang den tegnes i for-løkken? (Brug transform og scale)


#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg3.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render(n=n))
output_svg.close()
