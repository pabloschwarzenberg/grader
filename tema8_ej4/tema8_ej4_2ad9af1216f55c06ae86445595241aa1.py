def rot13(palabra):
    palabra=palabra.lower()
    abcdario= "abcdefghijklmnopqrstuvwxyz"
    resultado=""
    for letra in palabra:
        if letra in abcdario[:13]:
            resultado=resultado+abcdario[abcdario.index(letra)+13]
        elif letra in abcdario[13:]:
            resultado=resultado+abcdario[abcdario.index(letra)-13]
        else:
            resultado=resultado+letra
    return resultado