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
    num_palabras = 0
    num_car = 0
    largo_p = 0
    num_esp = 0
    num_punt = 0
    
    puntuacion = ".,"
    
    num_palabras = frase.split(" ")
    i=0
    while i < len(num_palabras):
        print(num_palabras[i])
    
    
    return num_palabras #, num_car, largo_p, num_esp, num_punt

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))