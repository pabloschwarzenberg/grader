def jerigonzo(string):
    vocals = "aeiouAEIOU"
    jerigonzo_text = ""
    for char in string:
        jerigonzo_text += char
        if char.lower() in vocals:
            jerigonzo_text += "p" + char
    return jerigonzo_text

if __name__ == "__main__":
    texto = input("Ingrese el texto a traducir a jerigonzo: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)