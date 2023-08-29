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
    caracteres = 0
    espacios = 0
    puntos = 0
    palabras = 0
    promedio = 0
    count = 0
    for i in range(0,len(hombre_imaginario)):
        count += 1
        if hombre_imaginario[i] == ' ' or hombre_imaginario[i] == '\n':
            count -= 1
            if hombre_imaginario[i] == '\n':
                palabras += 1
                if hombre_imaginario[i+1] == '\n':
                    palabras -= 1
            else:
                espacios += 1
                palabras += 1
        elif hombre_imaginario[i] == '.' or hombre_imaginario[i] == ',':
            puntos += 1
            count -= 1
        caracteres += 1
    promedio = count/palabras
    return palabras, caracteres, promedio, espacios, puntos

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
    pass
#print(numero de palabras, numero total de caracteres, largo promedio de las palabras, el numero de espacios, numero caracteres de puntacion)