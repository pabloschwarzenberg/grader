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
    L=list(frase)
    numero_caracteres=len(L)
    espacios=L.count(" ")
    puntuacion=L.count(".")
    puntuacion=puntuacion+L.count(",")
    puntuacion=puntuacion+L.count(":")
    puntuacion=puntuacion+L.count(";")
    puntuacion=puntuacion+L.count("¿")
    puntuacion=puntuacion+L.count("?")
    puntuacion=puntuacion+L.count("¡")
    puntuacion=puntuacion+L.count("!")
    puntuacion=puntuacion+L.count("(")
    puntuacion=puntuacion+L.count(")")
    puntuacion=puntuacion+L.count("-")
    puntuacion=puntuacion+L.count("_")
    puntuacion=puntuacion+L.count("''")

    frase=frase.replace(",", "")
    frase=frase.replace(".", "")
    frase=frase.replace("!", "")
    frase=frase.replace("¡", "")
    frase=frase.replace("¿", "")
    frase=frase.replace("?", "")
    frase=frase.replace(":", "")
    frase=frase.replace(";", "")
    frase=frase.replace("(", "")
    frase=frase.replace(")", "")
    frase=frase.replace("-", "")
    frase=frase.replace("_", "")
    L_0=frase.split( )
    numero_palabras=len(L_0)
    L_0=frase.split( )
    largo_palabras=0
    for i in range(len(L_0)):
        largo_palabras=largo_palabras+len(L_0[i])
    largo_promedio=(largo_palabras)/len(L_0)

    return numero_palabras, numero_caracteres,largo_promedio, espacios, puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         