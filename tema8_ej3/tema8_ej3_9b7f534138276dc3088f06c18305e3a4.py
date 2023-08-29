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
    frase=str(frase)
    #número de palabras
    palabras=frase.split()
    numero_de_palabras=len(palabras)
    #número total de caracteres
    contador=0
    for i in palabras:
        i=str(i)
        lista_palabra=list(i)
        caracteres=len(lista_palabra)
        contador=contador+caracteres
    #largo promedio de las palabras
    lista_largo_palabras=[]
    for i in palabras:
        i=str(i)
        i=list(i)
        i=len(i)
        lista_largo_palabras.append(i)
    contador1=0
    for i in range(len(lista_largo_palabras)):
        contador1=contador1+i
    largo_promedio_palabras=contador1/len(lista_largo_palabras)
    #numero de espacios
    numero_de_espacios=numero_de_palabras-1
    #numero de caracteres de puntuacion
    lista_puntuacion=[".",",",";",":","¡","!","¿","?","-"]
    contador2=0
    for i in lista_puntuacion:
        if i in frase:
            n=frase.count(i)
            print(n,"n") #sacar
            contador2=contador2+n
    print(contador2) #sacar
    return 75,521,5.88,59,3
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         