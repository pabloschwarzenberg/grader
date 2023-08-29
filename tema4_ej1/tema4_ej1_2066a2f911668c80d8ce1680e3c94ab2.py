import random
def ocultar_letras(palabra,cantidad):
    lista = []
    palabra = list(palabra)
    while cantidad != 0:
        uno = random.randint(1,len(palabra)-1)
        if uno not in lista:
            lista.append(uno)
            cantidad = cantidad -1
            palabra[uno] = "_"
    palabra = "".join(palabra)
    return palabra
            


def revisar_letra(palabra_secreta,palabra,letra):
    lista = list(palabra_secreta)
    palabra = list(palabra)
    if letra in lista:
        dos = palabra_secreta.find(",")
        palabra[dos] = letra
    palabra = "".join(palabra)
    
    return palabra

if __name__ == "__main__":
    pass
    palabra = input("Ingrese palabra: ")
    cantidad_letras = int(input("Ingrese cantidad de letras a ocultar: "))
    palabra_oculta = ocultar_letras(palabra, cantidad_letras)
    print("Palabra oculta:", palabra_oculta)

         