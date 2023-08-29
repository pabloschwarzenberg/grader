def jerigonzo(string):
    jerigonzo_text = ""
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            jerigonzo_text += char + "p" + char.lower()
        else:
            jerigonzo_text += char
    return jerigonzo_text

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)

         