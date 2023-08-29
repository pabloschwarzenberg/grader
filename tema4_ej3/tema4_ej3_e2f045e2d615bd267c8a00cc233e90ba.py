def jerigonzo(texto):
    resultado = ""
   
    for letra in texto:
        if letra.lower() in 'aeiou':
            resultado += letra + "p" + letra
        else:
            resultado += letra
    return resultado
texto_traducido = jerigonzo("estamos programando")        