__author__ = 'Domingo'
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
    signos=['1','2','3','4','5','6','7','8','9','0','.',',',':',';']
    puntuacion=0
    espacios=0

    caracteres=len(frase)
    lista=frase.split( )

    for i in frase:
        if i==" ":
            espacios+=1
    numero_palabras=espacios+1
    largo_promedio=(caracteres-espacios)/numero_palabras
    for j in frase:
        for i in signos:
            if j==i:
                puntuacion+=1
    return(numero_palabras,caracteres,largo_promedio,espacios,puntuacion)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))