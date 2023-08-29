def jerigonzo(string):
    transformar = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            transformar.append(letra)
    transformar = "".join(transformar)
    return transformar
if __name__ == "__main__":
    pass