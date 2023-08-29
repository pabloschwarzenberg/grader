def jerigonzo(string):
    texto_jerigonzo = ""
    vocales = "aeiouAEIOU"

    for letra in string:
        texto_jerigonzo += letra
        if letra in vocales:
            texto_jerigonzo += 'p' + letra.lower()

    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
