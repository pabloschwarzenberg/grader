def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def traducir_a_jerigonzo(texto):
    vocales = "aeiouAEIOU"
    texto_traducido = ""
    for letra in texto:
        texto_traducido += letra
        if letra in vocales:
            texto_traducido += "p" + letra.lower()
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
         