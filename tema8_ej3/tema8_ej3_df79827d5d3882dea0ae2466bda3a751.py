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
    frase = frase.lower()
    signos = [",",";",".",":","¿","?","!","¡"]
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","í","é","ó","ú"]
    
    palabras = 0
    caracteres = 0
    puntuacion = 0
    espacios = 0
    prom = 0
    
    for i in frase:
        if i in letras and frase[prom+1] not in letras:
            palabras += 1
        if i in letras:
            caracteres += 1
        if i in signos:
            puntuacion += 1
        if i not in letras and i not in signos:
            espacios += 1
        prom += 1
    frase_2 = list(frase)
    nuevo_2 = len(frase_2)
    espacio_2 = 0
    
    for e in frase_2:
        if e == " ":
            espacio_2 += 1
    promedio_largo = caracteres/palabras
    return palabras,nuevo_2,promedio_largo,espacio_2,puntuacion
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
from string import ascii_letters
         