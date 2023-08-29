def jerigonzo(string):
    vocales = "aeiouAEIOU"
    texto_traducido = ""
    for letra in string:
        texto_traducido += letra
        if letra in vocales:
            texto_traducido += "p" + letra.lower()
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)
