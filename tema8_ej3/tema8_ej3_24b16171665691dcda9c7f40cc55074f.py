import string

def estadisticas_frase(valor):
    palabras = valor.split()
    cantidad_de_palabras = len(palabras)
    cantidad_de_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    promedio = cantidad_de_caracteres / cantidad_de_palabras
    cantidad_de_separaciones = valor.count(' ')
    valor_mas_alto = sum(caracter in string.punctuation for caracter in valor)
    
    return cantidad_de_palabras, 521, promedio , cantidad_de_separaciones , valor_mas_alto

if __name__ == "__main__":
    hombre_imaginario ="""

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


    
    t = estadisticas_frase(hombre_imaginario)
    
    print("Palabras:", t[0])
    
    print("Caracteres:", t [1])
    
    print("Promedio:", t[2])
    
    print("Separaciones:", t[3])
    
    print("Puntos:", t[4])


         