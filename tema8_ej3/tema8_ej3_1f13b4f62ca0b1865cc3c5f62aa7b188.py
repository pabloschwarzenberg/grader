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
    espacios = frase.count(' ')
    frase = frase.lower().replace('\n', ' ')
    letras = list('abcdefghijklmnñopqrstuvwxyz áéíóú')
    frase_char = list(frase)
    palabras = []
    puntuación = []


    for char in frase_char: 
        if char in letras: 
            palabras.append(char)
        else: 
            puntuación.append(char)
    

    palabras = ''.join(palabras)
    palabras = palabras.strip().replace('  ', ' ').split(' ')
    cant_palabras = len(palabras)

    lenght = 0
    for palabra in palabras: 
        lenght += len(palabra)
    else: 
        lenght = lenght / cant_palabras

    
    

    estad = {
        'Número de Palabras': cant_palabras, 
        'N° Total Carácteres': len(frase),
        'Largo promedio palabras': round(lenght,2),
        'Número de espacios': espacios,
        'Número carácters puntuación': len(puntuación)
    }
    
    estadio = (cant_palabras,len(frase),round(lenght,2),espacios,len(puntuación))
    return estadio

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))