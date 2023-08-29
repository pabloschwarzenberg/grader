def jerigonzo(texto):
    traducido = ""
    vocales = "aeiouAEIOU"
    for letra in texto:
        if letra in vocales:
            traducido += letra + "p" + letra.lower()
        else:
            traducido += letra
    return traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    traducido = jerigonzo(texto)
    print("Texto traducido:", traducido)