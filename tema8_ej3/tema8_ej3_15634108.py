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
    numero_palabras=len(frase.split(" "))
    numero_caracteres=len(frase)
    numero_espacios=frase.count(" ")
    numero_puntuacion=frase.count(".")+frase.count(",")+frase.count(":")+frase.count(";")+frase.count("-")
    palabras=frase.replace(".","")
    palabras=palabras.replace(",","")
    palabras=palabras.replace(":","")
    palabras=palabras.replace(";","")
    caracteres=palabras.replace(" ","")
    lista_palabras=palabras.split(" ")
    lista_caracteres=list(caracteres)
    promedio=len(lista_caracteres)/len(lista_palabras)
    return numero_palabras,numero_caracteres,promedio,numero_espacios,numero_puntuacion


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         