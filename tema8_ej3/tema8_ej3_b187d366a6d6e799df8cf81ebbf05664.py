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
    caracter=len(hombre_imaginario)
    palabras=hombre_imaginario.split()
    i=0
    while i<len(palabras):
        palabra=palabras[i]
        if palabra==".":
            break
        i+=1
    espacios=len(hombre_imaginario.split(" "))-1
    especiales=len(hombre_imaginario.split("."))-1
    def pal(a):
        pa = []
        recolectador = ''
        separador = ' '
        for i in range(len(a)):
            recolectador += a[i]
            if a[i] == separador:
                pa.append(recolectador)
                recolectador = ''
    print(pal(hombre_imaginario))
    vf=441/75
    return i,caracter,vf,espacios, especiales
         