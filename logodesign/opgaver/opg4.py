import random
from jinja2 import Template
import os

dir = os.path.dirname(__file__)

#Åbn den svg-fil, der skal være template for loget
with open(os.path.join(dir,'opg4_template.svg')) as f:
    tmpl = Template(f.read())

## Opgave:
# 1. I svg-filen er der tegnet en lille cirkel. Prøv at klikke på cirklen. Den skulle gerne flytte sig og skifte størrelse undervejs. Det er lavet med to <animate>-tags i svg-koden. Man kan animere alle de forskellige attributter i svg-filen.
# 2. Prøv om du kan animere y-koordinaten også.
# 3. Man kan også animere bevægelse langs en kurve. Se dette eksempel: https://codepen.io/yshlin/pen/dxGlH
# 4. Prøv at lave op4_template om, så cirklen flytter sig langs en kurve, som du selv laver. Det kræver måske at du studerer <path>-tagget i svg: https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths Paths kan blive meget komplekse, og det er nok det mest avancerede tag-vi kommer til at bruge. Det behøver ikke være så komplekst, men prøv dig frem med nogle af eksemplerne fra det sidste link.

#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open(os.path.join(dir,'opg4.svg'), "w")
# I parentesen til funktionen "render" kan parametre sendes til jinja-skabelonen
n = output_svg.write(tmpl.render())
output_svg.close()
