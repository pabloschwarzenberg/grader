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

def caracteres(n):
    n = list(n)
    a = len(n)
    return a
def espacios(n):
    n = list(n)
    b = n.count(" ")
    return b
def puntuacion(n):
   n = list(n)
   a = "abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"
   d = 0
   print(n)
   for i in n:
       if i in a or i == " " or i =="\n":
           d = d
       else:
           d = d + 1
   return d
def palabras(n):
    n = n.split()
    a = len(n)
    return a
def largo_pro(n):
    a = palabras(n)
    n = list(n)
    r = "abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"
    d = 0
    for i in n:
        if i in r:
            d = d + 1
        if i not in r:
            d = d
    c = d/a
    return c
def estadisticas_frase(n):
    a = caracteres(n)
    b = espacios(n)
    c = puntuacion(n)
    d = palabras(n)
    e = largo_pro(n)
    return d,a,e,b,c

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         