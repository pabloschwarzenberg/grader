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
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    numero_caracteres = len(frase)
    b = frase.split( )
    for caracter in frase:
        if abecedario.find(caracter) == -1:
            c = frase.count(caracter)
    suma = []
    for palabra in b:
        suma.append(len(palabra))
    
    lista_frase = list(frase)
    for palabra in b:
        numero_espacios = lista_frase.count(' ')
    return len(b),len(frase),(sum(suma)-c)/len(b), numero_espacios, c