from random import randint


def ocultar_letras(palabra,cantidad):
    palabra2 = []
    palabra = list(palabra)
    basura = []
    while cantidad != 0:
        pl = randint(0,len(palabra)-1)
        if pl not in basura:
            basura.append(pl)
            cantidad = cantidad - 1
            palabra[pl] = "_"
    palabra = "".join(palabra)
        
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    l = list(palabra_secreta)
    palabra = list(palabra)
    if letra in l:
        encontrada = palabra_secreta.find("_")
        palabra[encontrada] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra

if __name__ == "__main__":
    pass
         