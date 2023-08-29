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
    cantidad_caracteres=len(frase)
    palabras=frase.replace("\n"," ").split(" ")
    i=0
    while i<len(palabras):
        if palabras[i]=='':
            palabras.pop(i)
        i=i+1
    cantidad_palabras=len(palabras)

    largo_promedio=0
    numero_espacios=frase.count(" ")
    caracteres_especiales=0
    for letra in frase:
        if not (letra.isalpha() or letra.isspace()):
            caracteres_especiales+=1
        elif letra.isalpha():
            largo_promedio+=1
    largo_promedio/=cantidad_palabras

    return cantidad_palabras,cantidad_caracteres,largo_promedio,numero_espacios,caracteres_especiales

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))