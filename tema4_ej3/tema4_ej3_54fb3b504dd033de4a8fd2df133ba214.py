def jerigonzo(string):
    lista = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            lista.append(letra)
    convertido = "".join(lista)
    return convertido

if __name__ == "__main__":
    pass
         