hombre_imaginario ="""
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
#calculo del numero de carcateres

def estadisticas_frase(frase):
   
    char = 0
    largo = 0
    caracter = 0
    nueva_frase = ''
    sum = 0
    palabras = 0
    res = frase.split()

    for num in res:
        palabras = palabras + 1

    for x in frase:
        if x != '.':
            nueva_frase += x
    l = nueva_frase.split()

    for num in l:
        sum += len(num)
        caracter = frase.count('.')
        largo = frase.count(' ')
        prom = sum / len(l)
    while frase[char:]:
        char += 1
    return(palabras,char,prom,largo,caracter)

print(estadisticas_frase(hombre_imaginario))