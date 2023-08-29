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

def estadisticas_frase(s):
    lista=s.split()
    cantidadp=len(lista)
    c=0
    for i in lista:
        c=c+len(i)
    promedio=c/cantidadp
    espacios=cantidadp-1

    return "{0},{1},{2},{3}".format(cantidadp, c, promedio, espacios)


    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         