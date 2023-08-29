def jerigonzo(string):
    resultado = ""
    vocales = "aeiouAEIOU"

    for letra in string:
        resultado += letra
        if letra.lower() in vocales:
            resultado += "p" + letra.lower()

    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)