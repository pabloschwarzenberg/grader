def jerigonzo(string):
    result = ""
    for char in string:
        if char.lower() in "aeiouáéíóú":
            result += char + "p" + char.lower()
        else:
            result += char
    return result

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
