hombre_imaginario = """
El hombre imaginario
vive en una mansion imaginaria
rodeada de arboles imaginarios
a la orilla de un rio imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcon imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
    hombre_imaginariol=list(hombre_imaginario)
    e=0
    puntuacion=0
    ultimo_espacio=0
    for i in range(len(hombre_imaginariol)):
        if hombre_imaginariol[i]==" ":
            e=e+1
            ultimo_espacio=i
        if hombre_imaginariol[i]==',' or hombre_imaginariol[i]=='.':
            puntuacion=puntuacion+1
        letras=i+1
        palabras=e+1
        promedio=(letras-e)/palabras
    return palabras,letras,promedio,e,puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         