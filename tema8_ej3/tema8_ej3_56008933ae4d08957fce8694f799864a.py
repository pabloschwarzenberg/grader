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
    letras=0
    espacios=0
    caracteres=0
    palabras=1
    puntuacion=0
    for i in range(0,len(frase)):
        if frase[i] in "abcdefghijklmnñopqrstuvwxyz":
            letras+=1
            caracteres+=1
        if frase[i]==" ":
            espacios+=1
            palabras+=1
            caracteres+=1
        if frase[i] in ".;:," and frase[i]!="...":
            puntuacion+=1
            caracteres+=1
    promedio=letras/palabras
    return (palabras,caracteres,promedio,espacios,puntuacion)

        

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         