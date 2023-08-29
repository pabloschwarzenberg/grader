#Creador: Daniel Ugarte
def jerigonzo(string):
    conv = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            conv.append(letra)
    conv = "".join(conv)
    return conv
         