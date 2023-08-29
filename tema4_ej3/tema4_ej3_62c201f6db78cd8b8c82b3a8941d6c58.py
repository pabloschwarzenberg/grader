def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra
    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    resultado = traducir_a_jerigonzo(texto)
    print("Texto original:", texto)
    print("Texto en jerigonzo:", resultado)
