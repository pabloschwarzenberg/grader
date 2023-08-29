def jerigonzo(texto):
    vocales = 'aeiouAEIOU'
    resultado = ''
    for caracter in texto:
        if caracter in vocales:
            resultado += caracter + 'p' + caracter
        else:
            resultado += caracter
    return resultado