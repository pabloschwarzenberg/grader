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

def estadisticas_frase(frase):
    x1=frase.split("\n")
    x2=" ".join(x1)
    x3=x2.split(" ")
    for i in x3:
        if i == "":
            x3.remove("")
    total=0
    especial=0
    for i in x3:
        for b in i:
            if b in ("."):
                especial+=1
            else:
                total+=1
    x4=frase.split(" ")
    x4=" ".join(x4)
    print(x4)
    contador=0
    for i in x4:
        if i in (" "):
            contador+=1
    promedio=total / len(x3)
    numero_palabras=len(x3)
    numero_caracteres=len(x2)
    return(numero_palabras,numero_caracteres,promedio,contador,especial)
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         