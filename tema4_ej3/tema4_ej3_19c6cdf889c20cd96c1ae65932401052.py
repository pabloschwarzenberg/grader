def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass

def jerigonzo(string):
    jerigonzo_text = ""
    vowels = "aeiouAEIOU"

    for char in string:
        jerigonzo_text += char
        if char in vowels:
            jerigonzo_text += "p" + char.lower()

    return jerigonzo_text

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_jerigonzo = jerigonzo(texto)
    print("Texto en Jerigonzo:", texto_jerigonzo)
    
#FIN