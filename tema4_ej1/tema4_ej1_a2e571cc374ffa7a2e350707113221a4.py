import random as rn


def ocultar_letras(palabra, cantidad):
    n = 0
    palabra_list = []
    cont = 0
    while n < len(palabra):
        palabra_list.append(palabra[n])
        n += 1
    while cont < cantidad:
        ind = rn.randrange(len(palabra))
        if palabra_list[ind] != "_":
            palabra_list[ind] = "_"
            cont += 1
    palabra = "".join(str(x) for x in palabra_list)
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    palabra_secreta_list = []
    palabra_list = []
    n = 0
    while n < len(palabra_secreta):
        palabra_secreta_list.append(palabra_secreta[n])
        palabra_list.append(palabra[n])
        n += 1

    repeticiones = palabra_secreta_list.count(letra)
    if repeticiones == 0:
        return palabra
    else:
        cont = 0
        while cont < len(palabra_secreta):
            if palabra_secreta_list[cont] == letra:
               palabra_list[cont] = letra
            cont += 1
    palabra = "".join(str(x) for x in palabra_list)
    return palabra

if __name__ == "__main__":
    pass
         