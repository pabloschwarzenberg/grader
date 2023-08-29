def jerigonzo(string):
    texto = []
    for i in string:
        for j in i:
            if j in "aeiouAEIOU":
                j = j + "p" + j
            texto.append(j)
    texto = "".join(texto)
    return texto

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    print(jerigonzo(texto))
    pass
         