def traducir_jerigonzo(texto):
    vocales = "aeiou"
    nuevo_texto = ""
    for letra in texto:
        if letra.lower() in vocales:
            nuevo_texto += letra.lower() + "p" + letra.lower()
        else:
            nuevo_texto += letra
    return nuevo_texto
if __name__ == "__main__":
    texto = "Hola, ¿cómo estás?"
    texto_traducido = traducir_jerigonzo(texto)
    print(texto_traducido)