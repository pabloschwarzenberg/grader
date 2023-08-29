def rot13(palabra):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    nuevo = ""
    for i in palabra:
        if i in alfabeto:
            if alfabeto.index(i) < 13:
                nuevo += alfabeto[alfabeto.index(i) + 13]
            else:
                nuevo += alfabeto[alfabeto.index(i) - 13]
        elif i in alfabeto.upper():
            if alfabeto.upper().index(i) < 13:
                nuevo += alfabeto.upper()[alfabeto.index(i) + 13]
            else:
                nuevo += alfabeto.upper()[alfabeto.index(i) - 13]
        else:
            nuevo += i
    palabra = nuevo
    return palabra


           