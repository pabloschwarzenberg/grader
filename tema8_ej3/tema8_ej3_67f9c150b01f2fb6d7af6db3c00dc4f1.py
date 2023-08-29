def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    
    caracteres_totales = len(s)
    
    suma_largos = sum(len(palabra.strip('.,?!')) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras if num_palabras > 0 else 0
    
    num_espacios = s.count(' ')
    num_puntuacion = sum(caracter in '.,?!' for caracter in s)
    
    return num_palabras, caracteres_totales, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    poema = """El hombre imaginario
vive en una mansion imaginaria
rodeada de arboles imaginarios
a la orilla de un rio imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcon imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""
    
    resultado = estadisticas_frase(poema)
    print("Numero de palabras:", resultado[0])
    print("Numero total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Numero de espacios:", resultado[3])
    print("Numero de caracteres de puntuacion:", resultado[4])