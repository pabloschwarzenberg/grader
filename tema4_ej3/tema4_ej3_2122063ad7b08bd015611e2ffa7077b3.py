def jerigonzo(texto):
    resultado = ""
    vocales = "aeiouAEIOU"
    for letra in texto:
        resultado += letra
        if letra in vocales:
            resultado += "p" + letra.lower()
    return resultado

if __name__ == "__main__":
    o = jerigonzo("estamos programando")
    print(o)
