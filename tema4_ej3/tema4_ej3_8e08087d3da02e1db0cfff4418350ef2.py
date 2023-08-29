def traducir_a_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_jerigonzo = ""
    for letra in texto:
        texto_jerigonzo += letra
        if letra.lower() in vocales:
            texto_jerigonzo += "p" + letra.lower()
    return texto_jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)

         