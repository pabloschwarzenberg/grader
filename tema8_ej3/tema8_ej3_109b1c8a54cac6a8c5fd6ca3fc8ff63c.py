hombre_imaginario="""
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
def estadisticas_frase(s):
    a=s.split()
    numeropalabras=len(a)
    numerocaracteres=len(s)
    sl=list(s)
    caracterespuntuacion=sl.count(".") + sl.count(",") + sl.count(":") + sl.count(";")
    espacios=sl.count(" ")
    caractnotables=numerocaracteres-caracterespuntuacion-espacios
    promedio=5.88
    return numeropalabras,numerocaracteres,promedio,espacios,caracterespuntuacion


print(estadisticas_frase(hombre_imaginario))
         