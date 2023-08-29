from random import randint as azar
def ocultar_letras(palabra,cantidad):
    contador = 0
    while contador != cantidad:
        posicion = azar(0,len(palabra)-1)
        if palabra[posicion] != "_":
            nueva_palabra = ""
            contador +=1
            for letra in range(len(palabra)):
                if posicion == letra:
                    nueva_palabra = nueva_palabra + "_"
                else:
                    nueva_palabra = nueva_palabra + palabra[letra]
            palabra = nueva_palabra
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    for i in range(len(palabra)):
        if palabra[i] == "_" and palabra_secreta[i] == letra:
            nueva_palabra = ""
            for j in range(len(palabra)):
                if i == j:
                    nueva_palabra = nueva_palabra + letra
                else:
                    nueva_palabra = nueva_palabra + palabra[j]
            palabra = nueva_palabra
    return palabra