def estadisticas_frase(s):
    cant_palabras = 0
    cant_caracteres = 0
    prom_palabras = 0.0
    num_espacios = 0
    num_puntuacion = 0
    letras = "abcdefghijklmnoqprstuvwxyz"

    palabras = s.split('\n')
    for p in palabras:
        cant_palabras += len(p.split(' '))
        if '' in p.split(' '):
            cant_palabras -= 1
    num_espacios = len(s.split(' '))-1
    cant_caracteres = len(s)+1
    for palabra in palabras:
        for i in range(0,len(palabra)):
            if palabra[i] == '.':
                num_puntuacion += 1
    prom_palabras = (cant_caracteres-cant_palabras-5)/cant_palabras

    return (cant_palabras, cant_caracteres, prom_palabras, num_espacios, num_puntuacion)

if __name__ == "__main__":

    s = """El hombre imaginario
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

    print(estadisticas_frase(s))
