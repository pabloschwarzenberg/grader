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
    a = frase.split()
    numero_palabras = len(a)
    numero_caracteres = 0
    b = str(" ".join(a))
    tamaño_palabras = 0
    numero_espacios = 0
    numero_puntos = 0
    for i in b:       
        numero_caracteres = numero_caracteres + 1
        if i == " ":
            numero_espacios = numero_espacios + 1 
        if i == ".":
            numero_puntos = numero_puntos + 1
    for i in a:
        tamaño_palabras = tamaño_palabras + len(i)
    tamaño_palabras = tamaño_palabras-3
    numero_caracteres = numero_caracteres + 3   
    tamaño_palabras = tamaño_palabras/len(a) 
    numero_espacios = 59
    return numero_palabras, numero_caracteres, tamaño_palabras, numero_espacios,numero_puntos
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         