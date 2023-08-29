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


def estadisticas_frase(s):
    n_espacios = 0
    n_punto = 0
    n_caracteres = 0
    lineas = s.split('\n')
    palabras = []

    for char in s:
        n_caracteres += 1

    for linea in lineas:
        n_espacios += linea.count(" ")
        for i in range(len(linea)):
            if not linea[i].isspace() and not linea[i].isalpha():
                n_punto += 1

        for i in range(len(linea)):
            if not linea[i].isspace() and not linea[i].isalpha():
                linea = linea.replace(linea[i], ".")

        linea = linea.replace(".", "")

        palabras_linea = linea.split()
        palabras += palabras_linea

    n_palabras = len(palabras)

    tamanos_palabras = [len(palabra) for palabra in palabras]


    largo_promedio = sum(tamanos_palabras) / len(tamanos_palabras)

    return (n_palabras, n_caracteres, largo_promedio, n_espacios, n_punto)
if __name__ == "__main__":
  print(estadisticas_frase(hombre_imaginario))