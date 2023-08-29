def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u']
    string_jerigonzo = ''

    for letra in string:
        string_jerigonzo += letra
        if letra.lower() in vocales:
            string_jerigonzo += 'p' + letra.lower()

    return string_jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
