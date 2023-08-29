def jerigonzo(string):
    jerigonzo_text = ""
    for char in string:
        if char.lower() in "aeiouáéíóú":
            jerigonzo_text += char + "p" + char.lower()
        else:
            jerigonzo_text += char
    return jerigonzo_text

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_jerigonzo = jerigonzo(texto)
    print("Texto en Jerigonzo:", texto_jerigonzo)
