def rot13(palabra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    MasLetras = ""
    for i in palabra:
        if i in letras:
            if letras.index(i) < 13:
                MasLetras += letras[letras.index(i)+13]
            else:
                MasLetras += letras[letras.index(i)-13]
        elif i in letras.upper():
            if letras.upper().index(i) < 13:
                MasLetras += letras.upper()[letras.index(i)+13]
            else:
                MasLetras += letras.upper()[letras.index(i) - 13]
        else:
            MasLetras +=1
    return MasLetras