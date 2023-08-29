def jerigonzo(string):
    jerigonzo_string = ""
    for char in string:
        if char.lower() in "aeiouáéíóú":
            jerigonzo_string += char + "p" + char.lower()
        else:
            jerigonzo_string += char
    return jerigonzo_string

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_jerigonzo = jerigonzo(texto)
    print("Texto en Jerigonzo:", texto_jerigonzo)

         