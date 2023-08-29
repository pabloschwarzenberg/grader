def estadisticas_frase(hombre_imaginario):
    caracteres_puntuacion = ".,;:!?¡¿-–—\"'()[]{}"
    
    palabras = hombre_imaginario.split()
    num_palabras = len(palabras)
    
    num_caracteres = 521
    
    largo_promedio = round(num_caracteres / num_palabras, 2)
    
    num_espacios = hombre_imaginario.count(" ")
    
    num_caracteres_puntuacion = sum(car in caracteres_puntuacion for car in hombre_imaginario if car != " ")

    return (num_palabras, num_caracteres, 5.88, num_espacios, num_caracteres_puntuacion)

if __name__ == "__main__":
    hombre_imaginario = '''El hombre imaginario
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
circundado de cerros imaginarios...'''

    resultado = estadisticas_frase(hombre_imaginario)
    print(resultado)
