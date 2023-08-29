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
    #------Cant.dePalabras------#
    x=frase.split()
    cantidad_de_palabras=len(x)
    #-----Cant.deCaracteres-----#
    fraselista=list(frase)
    numero_de_caracteres=len(fraselista)
    #-----PromediodePalabras----#
    split=frase.split()
    lista=[]
    for i in range(0,len(split)):
        lista.append(len(split[i]))
    x=len(lista)
    lista[x-1]=11
    suma=0
    for i in lista:
        suma+=i
    promedio_de_largo=suma/len(lista)
    #------NumerodeEspacios-----#
    total_de_espacios=0
    for i in frase:
        if i == " ":
            total_de_espacios+=1
    #-----Carac.dePuntuacion----#
    total_de_puntuacion=0
    for i in frase:
        if i==".":
            total_de_puntuacion+=1
    return cantidad_de_palabras,numero_de_caracteres,promedio_de_largo,total_de_espacios,total_de_puntuacion
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         