def rot13(palabra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    lista_letras_palabra = list(palabra)
    lista_letrasrot13 = []
    for letra in lista_letras_palabra:
        nletra = alfabeto.find(letra)
        if nletra != -1:
            if nletra>12:
                nletrarot13 = nletra-13
            else:
                nletrarot13 = nletra + 13
            letrarot13 = alfabeto[nletrarot13]
        else:
            letrarot13 = letra
        lista_letrasrot13.append(letrarot13)
    palabrarot13 = ''.join(lista_letrasrot13)
    return palabrarot13           