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
    lista_palabras = frase.split()
    lista_caracteres = []
    suma = 0
    for x in frase:
        lista_caracteres.append(x)
    caracteres_puntuacion = lista_caracteres.count(".")+lista_caracteres.count(",")+lista_caracteres.count(";") + lista_caracteres.count(":")
    numero_de_palabras = len(lista_palabras)
    contador_palabras = 0
    cantidad_n = lista_caracteres.count("\n")
    while contador_palabras < numero_de_palabras:  #suma de largo palabras contando puntos
        suma += len(lista_palabras[contador_palabras])
        contador_palabras += 1
    promedio = (suma-caracteres_puntuacion)/numero_de_palabras #promedio de largo palabras sin puntos
    numero_de_espacios = frase.count(" ")  #numero de espacios
    cantidad_caracteres = len(lista_caracteres) #numero de caracteres
    return  numero_de_palabras ,cantidad_caracteres , promedio , numero_de_espacios , caracteres_puntuacion



if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         