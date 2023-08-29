# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm

def rot13(palabra):
    letras_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    letras_2 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    palabra = list(palabra)
    palabra_nueva = []
    for i in palabra:
        if i in letras_1:
            letra = letras_1.index(i)
            letra_nueva = letras_2[letra]
            palabra_nueva.append(letra_nueva)
        else:
            letra = letras_2.index(i)
            letra_nueva = letras_1[letra]
            palabra_nueva.append(letra_nueva)
    palabra_nueva = "".join(palabra_nueva)
    return palabra_nueva

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)