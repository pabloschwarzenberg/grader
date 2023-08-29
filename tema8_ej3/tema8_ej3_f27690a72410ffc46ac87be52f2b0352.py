def estadisticas_frase(s):
    palabras = s.split()
    numero_palabras = len(palabras)
    numero_caracteres = sum(len(palabra.strip(".,!?")) for palabra in palabras)
    largo_promedio = numero_caracteres / numero_palabras
    numero_espacios = s.count(" ")
    caracteres_puntuacion = sum(1 for caracter in s if caracter in ".,!?")

    return numero_palabras, numero_caracteres, largo_promedio, numero_espacios, caracteres_puntuacion

if __name__ == "__main__":
    frase = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."
    resultado = estadisticas_frase(frase)
    print(resultado)
