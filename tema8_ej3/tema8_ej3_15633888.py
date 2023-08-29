
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

def estadisticas_frase(frase):
    a=frase.count(" ")+1
    b=len(frase)
    palabras=frase.split(" ")
    l_palabras=map(len,palabras)
    c=sum(l_palabras)/len(palabras)
    d=frase.count(" ")
    e=frase.count(".")
    return a,b,c,d,e
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         