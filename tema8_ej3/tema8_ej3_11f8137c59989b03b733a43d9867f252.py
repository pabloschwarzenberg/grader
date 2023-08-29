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
    #primero numero de palabras:
    palabras = frase.split()
    numero_palabras = len(palabras)
    return numero_palabras

    #numero de caracteres
    numero_caracteres = len(list(frase))
    return numero_caracteres

    #largo promedio de palabras
    

    #numero de espacios
    contador = 0
    S = list(frase)
    for i in range(len(numero_caracteres)):
        if S[i] == " ":
            contador += 1
    numero_espacios = contador 
    return numero_espacios
        
    #numero de caracteres de puntuacion
    caracteres_puntuacion = numero_caracteres - (numero_espacios + numero_palabras)
    return caracteres_puntuacion

    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         