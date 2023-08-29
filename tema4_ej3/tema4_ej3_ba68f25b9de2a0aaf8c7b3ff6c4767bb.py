def jerigonzo(string):
    traduccion = ""
    for char in string:
        if char.lower() in "aeiouáéíóú":
            traduccion += char + "p" + char.lower()
        else:
            traduccion += char
    return traduccion

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:")
    print(texto_traducido)
