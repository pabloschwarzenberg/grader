#def jerigonzo(string):
#    return string

#if __name__ == "__main__":
#    pass

def jerigonzo(string):
    Convertido = []
    for Palabra in string:
        for Letra in Palabra:
            if Letra in "aeiouAEIOU":
                Letra = Letra + "p"+ Letra
            Convertido.append(Letra)
    Convertido = "".join(Convertido)
    return Convertido