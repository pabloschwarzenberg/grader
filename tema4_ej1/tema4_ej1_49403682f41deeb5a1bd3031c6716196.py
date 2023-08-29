import random as rd

def ocultar_letras(palabra,cantidad):
    La=len(palabra)
    palabra2 = list(palabra)
    while cantidad !=0:
        posicion = rd.randint(0,La-1)
        if palabra2[posicion]!="_":
            palabra2[posicion]="_"
            cantidad-=1
    return palabra2

def listaAcadena(lista):
    cadena =" "
    for letras in cadena:
        cadena = cadena + letras
    return cadena

def posisionesCadena(cadena,letra):
    largo = len(cadena)
    posiciones = []
    for indice in range(largo):
        if cadena[indice] == letra:
            posiciones.append(indice)
    return posiciones

def revisar_letra(palabra_secreta,palabra,letra):
    posiciones=posisionesCadena(palabra,"_")
    palabra2 = list(palabra)
    for i in posiciones:
        if palabra_secreta[i] == letra:
            palabra2[i] = letra
    cadena = "".join(palabra2)
    return cadena