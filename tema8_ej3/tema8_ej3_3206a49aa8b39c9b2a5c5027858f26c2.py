hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

def line(words, horiz_pos = -50):
    x,y = tina.pos()
    tina.goto(max(horiz_pos, -190), y)
    tina.write(words)
    x,y = tina.pos()
    tina.goto(x, y - 25)

def by(author):
    x,y = tina.pos()
    tina.goto(x + 70, max( -190, y -30))
    tina.write(author)
    x,y = tina.pos()
    tina.goto(0, y)

tina.goto(-50, 190)
line("Snow in my shoe")
line("Abandoned")
line("Sparrow's nest")
by("Jack Kerouac")
         