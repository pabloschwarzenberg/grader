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
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    palabras = frase.split()
    total_palabras = len(palabras)
    total_caracteres = len(frase)#0
    carac_sin_espacio = 0
    caracteres_p = 0

    for palabra in palabras:
        carac_sin_espacio += len(palabra)
        for caracter in palabra:
            if caracter.lower() not in letras:
                caracteres_p += 1 

    largo_promedio = (carac_sin_espacio-caracteres_p)/total_palabras
    total_espacios = 0

    for caracter in frase:
        if caracter == " ":
            total_espacios += 1

    return total_palabras, total_caracteres, largo_promedio, total_espacios, caracteres_p

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))