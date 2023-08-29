def jerigonzo(string):
    resultado = ""
    vocales = "aeiouAEIOU"
    for letra in string:
        resultado += letra
        if letra in vocales:
            resultado += "p" + letra
    return resultado

if __name__ == "__main__":
    texto_ingresado = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto_ingresado)
    print("Texto traducido:", texto_traducido)