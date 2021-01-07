import random
from jinja2 import Template


#Åbn den svg-fil, der skal være template for loget
with open('test.svg') as f:
    tmpl = Template(f.read())

#n tilfældige punkter
n=10
xs = [random.randint(10,190) for _ in range(n)]
ys = [random.randint(10,190) for _ in range(n)]
points = [(xs[i],ys[i]) for i in range(len(xs))]

#Tilfældigt centerpunkt
cpos = [random.randint(300,350), random.randint(40,80)]

#Åbn svg-filen hvor logoet skal gemmes.
output_svg = open("result.svg", "w")
n = output_svg.write(tmpl.render(cpos=cpos, points=points))
output_svg.close()
