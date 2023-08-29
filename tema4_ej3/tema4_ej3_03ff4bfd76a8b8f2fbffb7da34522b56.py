def jerigonzo(texto):
    vocales = "aeiouAEIOU"
    jerigonzo_texto = ""
    for letra in texto:
        if letra in vocales:
            jerigonzo_texto += letra + "p" + letra.lower()
        else:
            jerigonzo_texto += letra
    return jerigonzo_texto
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_jerigonzo = jerigonzo(texto)
    print("El texto en jerigonzo es:", texto_jerigonzo)
