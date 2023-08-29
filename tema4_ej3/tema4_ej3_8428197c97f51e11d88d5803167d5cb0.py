def traducir_a_jerigonzo(texto):
    resultado = ""
    for letra in texto:
        if letra.lower() in "aeiou":
            resultado += letra + "p" + letra.lower()
        else:
            resultado += letra
    return resultado
         