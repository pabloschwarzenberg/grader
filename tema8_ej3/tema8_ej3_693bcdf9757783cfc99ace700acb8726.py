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
    palabras = 0
    caracteres = 0
    espacios = 0
    caracter = 0
    nueva_frase = ''
    suma = 0

    o = s.split()

    for numero in o:
        palabras = palabras + 1

    for x in s:
        if x != '.':
            nueva_frase += x
    l = nueva_frase.split()

    for num in l:
        suma += len(num)
    promedio = suma / len(l)


    caracter = s.count('.')

    espacios = s.count(' ')

    while s[caracteres:]:
        caracteres += 1


    return(palabras,caracteres,promedio,espacios,caracter)

print(estadisticas_frase(hombre_imaginario))
