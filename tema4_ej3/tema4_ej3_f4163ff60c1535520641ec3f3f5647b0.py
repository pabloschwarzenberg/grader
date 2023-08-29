def jerigonzo(string):
    jerigonzo_texto = ""
    vocales = "aeiouáéíóú"
    for char in string:
        if char.lower() in vocales:
            jerigonzo_texto += char + "p" + char.lower()
        else:
            jerigonzo_texto += char
    return jerigonzo_texto

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a Jerigonzo:", texto_traducido)