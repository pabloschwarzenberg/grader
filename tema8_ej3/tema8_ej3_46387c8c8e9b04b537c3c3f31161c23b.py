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
    
    laola = frase.split()
    cantidadpalabras = len(laola)
    
    fraselista = list(frase)
    caracter = len(fraselista)
    
    split = frase.split()
    lista = []
    for i in range(0,len(split)):
        lista.append(len(split[i]))
    laola = len(lista)
    lista[laola - 1] = 11
    suma = 0
    for i in lista:
        suma += i
    promedio = suma/len(lista)
    
    totalspace = 0
    for i in frase:
        if i == " ":
            totalspace += 1
    
    totalpoints = 0
    for i in frase:
        if i == ".":
            totalpoints += 1
    return cantidadpalabras,caracter,promedio,totalspace,totalpoints