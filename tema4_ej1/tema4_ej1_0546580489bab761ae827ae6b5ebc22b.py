import random


def ocultar_letras(palabra, cantidad):
    lista = list(palabra)
    while cantidad > 0:
        letra = random.randint(0,len(lista) - 1)
        if lista[letra] == "_":
            letra = random.randint(0,len(lista) - 1)
        else:
            lista[letra] = "_"
        cantidad -= 1
    palabra = ''.join(lista)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    secreto = list(palabra_secreta)
    mostrado = list(palabra)
    for x in secreto:
      if x == letra:
        mostrado[secreto.index(x)] = x
        secreto[secreto.index(x)] = "_"
    palabra = ''.join(mostrado)
    return palabra


if __name__ == "__main__":
    pass
         