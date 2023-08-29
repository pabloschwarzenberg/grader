def rot13(palabra):
    if palabra == palabra.upper():
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        abc = "abcdefghijklmnopqrstuvwxyz"
    k=13
    cifrad=""
    for caracter in palabra:
        if caracter in abc:
            cifrad += abc[(abc.index(caracter)+k)%(len(abc))]
        else:
            cifrad+=caracter
    return cifrad
