alphabet = 'abcdefghijklmnopqrstuvwxyz'


def rot13(palabra):
    palabra = palabra.lower()

    # the encrypted message
    result = ''

    # Replace each letter in the string with a letter which is 13 positions further
    for char in palabra:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) + 13) % 26]
        else:
            result += char
    return result
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)