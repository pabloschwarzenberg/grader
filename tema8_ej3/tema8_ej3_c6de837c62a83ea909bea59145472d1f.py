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
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

    frase = frase.lower()
    fraseOriginal = frase
    frase = frase.strip('.')
    frase = frase.split()
    CantidadDePalabras = len(frase)
    CantidadDeCaaracteres = len(fraseOriginal)
    palabras = []
    for palabra in frase:
        if palabra not in palabras:
            for letra in palabra:
                if letra not in abc:
                    break

        palabras.append(palabra)

    prom = 0
    print(palabras)
    for elemento in palabras:
        prom += len(elemento)

    prom = (prom / len(palabras))

    espacios = 0
    puntos = 0
    for x in fraseOriginal:
        if x == ' ':
            espacios +=1
        if x == '.':
            puntos += 1



    return CantidadDePalabras, CantidadDeCaaracteres, prom, espacios, puntos
    
   
   
   
   
   
   
   
   
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))