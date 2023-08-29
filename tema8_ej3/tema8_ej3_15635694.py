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

#retorne el número de palabras, el número total de caracteres,
#el largo promedio de las palabras,
#el número de espacios, y el número de caracteres de puntuación

def estadisticas_frase(frase):
    palabras=len(frase.split())
    return palabras    
def ntcarac(frase):
    carac=len(frase)
    return carac
def largoprom(frase):
    palabra=frase.split()
    tt=0
    for i in palabra:
        t=len(palabra)
        tt+=t
    lp = tt/(len(palabra))
    return lp
def ndespacios(frase):
    i=0
    n=str(" ")
    for j in frase:
        if j==n:
            i+=1
    return i
def ndepuntos(frase):
    i=0
    n=str(".")
    for j in frase:
        if j==n:
            i+=1
    return i
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
    print(ntcarac(hombre_imaginario))
    print(largoprom(hombre_imaginario))     
    print(ndespacios(hombre_imaginario))
    print(ndepuntos(hombre_imaginario))   

