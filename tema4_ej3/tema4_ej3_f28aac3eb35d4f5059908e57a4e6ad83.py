def jerigonzo(texto):
    vocales = "aeiouAEIOU"
    texto_traducido = ""
    for letra in texto:
        texto_traducido += letra
        if letra in vocales:
            texto_traducido += "p" + letra.lower()
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido: ", texto_traducido)