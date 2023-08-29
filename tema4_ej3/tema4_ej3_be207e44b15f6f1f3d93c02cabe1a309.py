def jerigonzo(texto):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    resultado = ""
    for letra in texto:
        if letra in vocales:
            resultado += letra + "p" + letra.lower()
        else:
            resultado += letra
    return resultado
