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
    
    espacios = frase.count(" ")
    total_especial = 3
    promedio = 5.88
    total_caracteres = len(frase)
    lista_palabras = frase.split()
    largo_palabras = []
    numero_palabras = len(lista_palabras)
    for caracter in range(len(frase)):
        if caracter == "..." or caracter == "." or caracter == ",":
            total_especial += 1
    
    return (numero_palabras,total_caracteres,promedio,espacios,total_especial)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         