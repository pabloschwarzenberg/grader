def jerigonzo(string):
    vocal = "aeiouAEIOU"
    traduccion = ""
    for letra in string:
        traduccion += letra
        if letra in vocal:
            traduccion += "p" + letra.lower()
    return traduccion
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    traduccion = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", traduccion)