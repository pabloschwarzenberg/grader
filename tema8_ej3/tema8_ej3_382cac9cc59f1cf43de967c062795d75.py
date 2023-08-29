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

def estadisticas_frase(s):
    caracteresTotal= len(s)
    lista=list(s)
    sumaDeCaracteres=len(s)
    espacios=0
    caracteresDePuntuacion=0
    for elemento in lista:
        elemento=elemento
        if elemento is " ":
            sumaDeCaracteres-=1
            espacios+=1

        if elemento is ",":
            sumaDeCaracteres-=1
            caracteresDePuntuacion+=1

        if elemento is ".":
            sumaDeCaracteres-=1
            caracteresDePuntuacion+=1
    listaPalabras=[]
    palabra=""
    i=0
    while i<len(s):
        if s[i] is not " ":
            if s[i] is not ",":
                if s[i]is not ".":
                    if s[i] is not "\n":
                        palabra+=str(s[i])
                        i+=1
                        if i<len(s):
                            if s[i] is ",":
                                listaPalabras.append(palabra)
                                palabra=""
                            if s[i] is ".":
                                listaPalabras.append(palabra)
                                palabra=""
                            if s[i] is " ":
                                listaPalabras.append(palabra)
                                palabra=""
                            if s[i] is "\n":
                                listaPalabras.append(palabra)
                                palabra=""
                        if i ==len(s):
                            if len(palabra) != 0:
                                listaPalabras.append(palabra)
                    else:
                        i+=1
                else:
                    i+=1
            else:
                i+=1
        else:
            i+=1
    numeroDePalabras=len(listaPalabras)
    largo_palabras=0
    for palabra in listaPalabras:
        largo_palabras=largo_palabras+len(palabra)

    largoPromedio=largo_palabras/numeroDePalabras
    return numeroDePalabras,caracteresTotal,largoPromedio,espacios,caracteresDePuntuacion
