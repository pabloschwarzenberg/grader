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
    espacios=0
    p=0
    for x in frase:
        if x == " ":
            espacios+= 1
        elif not x.isalpha() and x !="\n":
            p+=1
    palabras=frase.split()
    car=len(frase)
    largep=0
    for x in palabras:
        if x.isalpha():
            largep+=len(x)
        else:
            largep+= len(x.strip('.'))
    largep/=len(palabras)
    return len(palabras),car,largep,espacios,p

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         