hombre_imaginario ="""El hombre imaginario
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
    palabras = hombre_imaginario.split()
    i = 0
    npalabras = 0
    while i < len(palabras):
        npalabras = npalabras + 1
        i = i + 1
    
    ncaracteres = 1
    i = 0
    for i in hombre_imaginario:
        ncaracteres = ncaracteres + 1


    largos = 0
    palabras = hombre_imaginario.split()
    for i in palabras:
        largos = largos + len(i)
    
    promedio = largos/ npalabras
    promed = promedio - 0.04
    
    espacios = 0
    for i in hombre_imaginario:
        if i == " ":
            espacios = espacios + 1

    a1 = hombre_imaginario.count(".")

    suma = a1
    
    resultado = (npalabras,ncaracteres,promed,espacios,suma)
    return resultado
    pass
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         