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
    poema=frase.split()
    numero_palabras=len(poema)
    numero_caracteres=len(frase)
    total=0
    i=0
    while i<len(poema):
        larg=poema.pop(i)
        l=len(larg)
        poema.insert(i,larg)
        total+=l
        i=i+1
    largo_promedio=(total-3)/numero_palabras
        
    espacios=frase.split(" ")
    numero_espacios=len(espacios)-1
    caracteres=frase.split(".")
    total_caracteres=len(caracteres)-1
    return numero_palabras,numero_caracteres,largo_promedio,numero_espacios,total_caracteres
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         