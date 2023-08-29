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
    #numero de caracteres
    numero_de_carateres=len(frase)
    #largo promedio de las palabras
    lista_poema=frase.split(" ")
    suma=0
    for i in lista_poema:
      suma=suma+len(i)
    largo_promedio_palabras=suma/len(lista_poema)
    #número de espacios
    numero_de_espacios=frase.count(" ")
    #numero de caracteres de puntuacion
    abecedario="abcdefghijklmnopqrstuvwxyz"
    for i in abecedario:
      frase.replace(i,"")
      frase.replace(" ","")
    numero_de_caracteres_de_puntuacion=len(frase)
    a=numero_de_carateres
    b=largo_promedio_palabras
    c=numero_de_espacios
    d=numero_de_caracteres_de_puntuacion
    return a,b,c,d

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         