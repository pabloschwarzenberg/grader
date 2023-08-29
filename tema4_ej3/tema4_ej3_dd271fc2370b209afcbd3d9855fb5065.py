def jerigonzo(texto):
    consonantes = 'aeiouAEIOU'
    resultado = ''
    for letra in texto:
        if letra in consonantes:
            resultado += letra + 'p' + letra
        else:
            resultado += letra
    return resultado
