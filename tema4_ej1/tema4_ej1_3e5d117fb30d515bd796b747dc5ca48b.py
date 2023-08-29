import random


def buscarTodas(a, b):
    a_l = list(a)
    indices = []
    while a_l.count(b) != 0:
        indices.append(a_l.index(b))
        a_l[a_l.index(b)] = 0
    return indices


def ocultar_letras(palabra,cantidad):
    palabra = list(palabra)
    i=0
    while i != cantidad:
        indice = random.randint(0,len(palabra)-1)
        if palabra[indice] == '_':
            pass
        else:
          palabra[indice] = '_'
          i += 1
    palabra = ''.join(palabra)
    return palabra


def revisar_letra(palabra_secreta,palabra,letra):
    if letra == palabra_secreta:
        return palabra_secreta
    else:
        palabra_secreta = list(palabra_secreta)
        palabra = list(palabra)
        if palabra_secreta.count(letra) == 0:
            return palabra
        else:
            indices = buscarTodas(palabra_secreta, letra)
            for i in indices:
                palabra[i] = letra
            palabra = ''.join(palabra)
            return palabra


if __name__ == "__main__":
    pass
         