def rot13(palabra):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_palabra = ""

    for i in palabra:
        alphabet_index = alphabet.index(i) + 13

        if alphabet_index <= 25:
            encrypted_palabra += alphabet[alphabet_index]
        else:
            encrypted_palabra += alphabet[alphabet_index - 26]

    return encrypted_palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           