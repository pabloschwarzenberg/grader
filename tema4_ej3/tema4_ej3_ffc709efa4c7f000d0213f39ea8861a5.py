def jerigonzo(string):
    convertir = []
    for palabra in string:
        for L in palabra:
            if L in "aeiouAEIOU":
                L = L + "p"+ L
            convertir.append(L)
    convertir = "".join(convertir)
    return convertir
