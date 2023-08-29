def jerigonzo(texto):
    vocales=["a","e","i","o","u"]
    letras=list(texto)
    for index, letter in enumerate(letras):
        if letter in vocales:
            letras.insert(index+1,"p"+letter)
    texto2="".join(letras)
    return texto2




if __name__ == "__main__":
    pass
         