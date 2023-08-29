def rot13(palabra):

    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ROT = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    CODE = ""

    for i in range(len(palabra)):
        letra = palabra[i]
        if letra in ABC:
            INDEX = ABC.find(letra)
            CODE += ROT[INDEX]
    return CODE
           