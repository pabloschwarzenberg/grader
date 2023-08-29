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

    sin_salto = frase.replace('\n', ' ')
    sin_salto = sin_salto.replace('  ', ' ')
    lista = sin_salto.split(' ')
    lista.pop(0)
    sin_espacio = sin_salto.replace(' ', '')

    
    suma = 0
    for i in lista:
        if '...' not in i:
            suma += len(i)
        else:
            suma += len(i) - 3
    promedio = round(suma / len(lista), 2)

    espacio = 0
    punto = 0
    for j in frase:
        if j == ' ':
            espacio += 1
        elif j == '.':
            punto += 1            

    return len(lista), len(frase), promedio, espacio, punto

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         