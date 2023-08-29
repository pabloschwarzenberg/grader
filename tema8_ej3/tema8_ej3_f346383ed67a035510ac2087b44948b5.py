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
    numero_palabras = len(frase.split())
    caracteres = len(frase)
    for i in frase:
        if i.isalpha():
            letras += 1
        else:
            pass
    letras = letras/numero_palabras
    espacios = frase.count(' ')
    caracteres_puntuacion = frase.count('.')
    return numero_palabras,caracteres,letras,espacios,caracteres_puntuacion
    
    
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         