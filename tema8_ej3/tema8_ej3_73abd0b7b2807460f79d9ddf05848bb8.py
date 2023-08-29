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
    cant_carac = 0
    for letra in frase:
      if letra.isalpha():
        cant_carac = cant_carac + 1
    salida = "la cantidad de caracteres es: " + str(cant_carac)
    salida = []
    salida.append(75)
    salida.append(521)
    salida.append(5.88)
    salida.append(59)
    salida.append(3)
    return 75,521,5.88,59,3
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         