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
    nro=0
    espacios=0
    puntuacion=0
    palabra=frase.replace(".","")
    palabras=palabra.replace(",","")
    palabras2=palabras.split()
    contador=0
    print(palabras2)
    for j in palabras2:
        contador+=len(j)
    promedio=contador/len(palabras2)
    for i in frase:
        nro+=1
        if i ==" ":
            espacios+=1
        elif i=="," or i==".":
            puntuacion+=1
    return (len(palabras2),nro,promedio,espacios,puntuacion)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))