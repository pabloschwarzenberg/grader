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
    texto_traducido = jerigonzo(texto)
    print("Texto traducido al jerigonzo:", texto_traducido)
