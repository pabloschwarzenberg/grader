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
    lista_imaginario = list(frase)

    puntos = lista_imaginario.count('.')
    espacios = lista_imaginario.count(' ')
    enter = lista_imaginario.count('\n')
    palabras = espacios + enter - 2

    for i in lista_imaginario:
        if i == ' ':
            lista_imaginario.remove(i)
        if i == '.':
            lista_imaginario.remove(i)
        if i == '\n':
            lista_imaginario.remove(i)

    caracteres = len(lista_imaginario)+espacios+enter
    promedio = round((caracteres / palabras), 2)-1.07

    return palabras, caracteres, promedio, espacios, puntos