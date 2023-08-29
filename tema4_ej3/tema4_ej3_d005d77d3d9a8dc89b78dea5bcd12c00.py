def jerigonzo(string):
    jerigonzo_text = ""
    for char in string:
        if char.lower() in "aeiouáéíóú":
            jerigonzo_text += char + "p" + char.lower()
        else:
            jerigonzo_text += char
    return jerigonzo_text

if __name__ == "__main__":
    texto = "Hola, cómo estás?"
    texto_jerigonzo = jerigonzo(texto)
    print("Texto original: {texto}")
    print("Texto en jerigonzo: {texto_jerigonzo}")
