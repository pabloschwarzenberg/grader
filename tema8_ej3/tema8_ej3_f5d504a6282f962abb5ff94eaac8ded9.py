import string

def estadisticas_frase(s):
    palabras = s.split()  # Dividir el texto en palabras utilizando los espacios como separadores
    num_palabras = len(palabras)  # Contar el número de palabras
    
    caracteres_totales = sum(len(palabra) for palabra in palabras)  # Sumar la longitud de cada palabra
    
    # Calcular el largo promedio de las palabras
    largo_promedio = caracteres_totales / num_palabras if num_palabras > 0 else 0
    
    num_espacios = s.count(' ')  # Contar el número de espacios
    
    # Crear una cadena de caracteres de puntuación utilizando la librería string
    caracteres_puntuacion = string.punctuation
    
    # Contar el número de caracteres de puntuación que no son letras ni espacios
    num_caracteres_puntuacion = sum(s.count(caracter) for caracter in caracteres_puntuacion if caracter not in (' ', "'"))
    
    return num_palabras, caracteres_totales, largo_promedio, num_espacios, num_caracteres_puntuacion

if __name__ == "__main__":
    texto = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."
    resultado = estadisticas_frase(texto)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
