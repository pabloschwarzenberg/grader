def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    resultado = ""
    for char in string:
        if char in vocales:
            resultado += char + 'p' + char
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido al Jerigonzo:", texto_traducido)
