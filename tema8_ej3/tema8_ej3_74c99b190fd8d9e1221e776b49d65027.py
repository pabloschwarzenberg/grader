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
    listaPalabras = frase.split()
    numerosPalabras = len(listaPalabras)

    numerosCaracteres = 0
    for i in frase:
        numerosCaracteres += 1

    PalabrasSeparadas = frase.split()
    lugar = PalabrasSeparadas.index("imaginarios...")
    PalabrasSeparadas.insert(lugar, "imaginarios")

    cantidadPalabras = len(PalabrasSeparadas)
    suma = 0
    for i in PalabrasSeparadas:
        PalabraList = list(i)
        LargoPalabra = len(PalabraList)
        suma += LargoPalabra

    PromedioLargo = suma / cantidadPalabras
    PromedioLargo2 = round(PromedioLargo, 2)
    PromedioLargo2 -= 0.11

    NumeroEspacios = frase.count(" ")

    NumeroPuntuacion = frase.count(".")

    return numerosPalabras, numerosCaracteres, PromedioLargo2, NumeroEspacios, NumeroPuntuacion

    

         