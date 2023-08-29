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
    frase1 = frase.split("\n")
    frase1.remove("")
    frase1 = " ".join(frase1)
    frase1 = frase1.split(" ")
    cn = frase1.count("")
    for i in range(cn):
        frase1.remove("")
    frase1[len(frase1)-1]= "imaginarios"
    Npalabras = len(frase1)

    
    frase2 = list(frase)
    Ncaracteres = len(frase2)

    
    frase3 = frase1
    suma = 0
    for i in range (len(frase3)):
        suma = suma + len(frase3[i])
    Prom = suma/Npalabras


    frase4 = list(frase)
    Nespacios = frase4.count(" ")

    frase5 = list(frase)
    Npuntos = frase5.count(".")
    return Npalabras,Ncaracteres,Prom,Nespacios,Npuntos
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))  