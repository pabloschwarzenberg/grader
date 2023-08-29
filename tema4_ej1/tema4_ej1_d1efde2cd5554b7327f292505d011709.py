import random

def ocultar_letras(palabra,cantidad):
    for i in range(0,cantidad+1):
        n = random.randint(0,len(palabra)-1)
        palabra = list(palabra)
        palabra[n]= "_"
        palabra = ''.join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    if palabra_secreta.count(letra) != 0:
        if palabra.count(letra) != palabra_secreta.count(letra):
            for i in range(len(palabra)):
                if palabra_secreta[i] == letra:
                    palabra = list(palabra)
                    palabra[i] = letra
                    palabra = "".join(palabra)
    return palabra

if __name__ == "__main__":
    loop = 1
    listapalabras = ["felino","helicoptero","suelo","esternocleidomastoideo","lepidoptero"]
    n = random.randint(0,len(listapalabras)-1)
    palabra_secreta =listapalabras[n]
    nletras = random.randint(1,len(palabra_secreta)-1)
    palabra = ocultar_letras(palabra_secreta,nletras)
    print(palabra)
    while loop == 1:
        letra = input("ingrese letra: ")
        newpalabra = revisar_letra(palabra_secreta,palabra, letra)
        print(newpalabra)
        palabra = newpalabra
        if palabra_secreta == palabra:
            print("win!")
            loop = 0
        elif letra.isalpha == False:
            print("por favor ingrese letra del alfabeto")