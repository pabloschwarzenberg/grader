def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"

    for caracter in texto:
        jerigonzo += caracter
        if caracter in vocales:
            jerigonzo += "p" + caracter.lower()

    return jerigonzo
if __name__ == "__main__":
    texto = "Hola, cómo estás?"
    resultado = traducir_a_jerigonzo(texto)
    print("Texto original: " + texto)
    print("Texto en jerigonzo: " + resultado)
