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
    frase2=frase.replace("\n"," ")
    frase2=frase2.replace("  "," ")
    palabras=list(frase2)
    y=palabras.count(".")
    while not y==0:
        palabras.remove(".")
        y-=1
    palabras.remove(palabras[0])
    palabras2="".join(palabras)
    palabras2=palabras2.split(" ")
    print(palabras2)
    palabras3=len(palabras2)
    letras=list(frase)
    letras=len(letras)
    contador=0
    sumatoria=0
    frase=list(frase)
    for n in palabras2:
        sumatoria+=len(n)
        contador+=1
    promedio=sumatoria/contador
    espacios=frase.count(" ")
    puntos=frase.count(".")+frase.count(",")
    
    return palabras3,letras,promedio,espacios,puntos
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         