def jerigonzo(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for letra in texto:
        if letra in vocales:
            resultado += letra + "p" + letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    print(jerigonzo(texto))

         