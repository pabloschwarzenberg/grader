def jerigonzo(string):
    convert = []
    for palabra in string:
        for letras in palabra:
            if letras in "aeiouAEIOU":
                letras = letras + "p"+ letras
            convert.append(letras)
    convert = "".join(convert)
    return convert