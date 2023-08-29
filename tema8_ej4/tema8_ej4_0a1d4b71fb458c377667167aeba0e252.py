def rot13(palabra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''
    for caracter in palabra:
        if caracter.lower() in alfabeto:
            indice = alfabeto.index(caracter.lower())
            indice_rot13 = (indice + 13) % 26
            if caracter.isupper():
                resultado += alfabeto[indice_rot13].upper()
            else:
                resultado += alfabeto[indice_rot13]
        else:
            resultado += caracter
    return resultado
