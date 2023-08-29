def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    for caracter in texto:
        jerigonzo += caracter
        if caracter.lower() in "aeiouáéíóú":
            jerigonzo += "p" + caracter.lower()
    return jerigonzo

if __name__ == "__main__":
    texto = "Hola, cómo estás?"
    resultado = traducir_a_jerigonzo(texto)
    print(resultado)
