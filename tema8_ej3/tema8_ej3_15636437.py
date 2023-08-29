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
    palabras=frase.split()
    n_palabras=len(palabras)
    contador=0
    for palabra in palabras:
        for letras in palabra:
            contador+=1
    return "el número de palabras es ",n_palabras,"el numero de caracteres es ",contador

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         