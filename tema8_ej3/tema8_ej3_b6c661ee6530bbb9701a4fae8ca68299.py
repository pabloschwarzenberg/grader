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
    lista = frase.split()
    string = " ".join(lista)
    strSinPuntos = string.split(".")
    ListaFinal = strSinPuntos[0].split()
    numeroPalabras = len(frase.split())
    numeroCaracteres = len(frase)
    numeroEspacios = frase.count(" ")
    numeroPuntuacion = frase.count(".")
    sinPuntos = frase.split(".")
    caracteresEnCadaPalabra = []
    for element in ListaFinal:
        caracteresEnCadaPalabra.append(len(element))
    
    promedioLargo = sum(caracteresEnCadaPalabra) / numeroPalabras

    return numeroPalabras, numeroCaracteres, promedioLargo, numeroEspacios, numeroPuntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         