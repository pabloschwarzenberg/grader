def rot13(palabra):
    result = ""
    for letter in palabra:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - 65 + 13) % 26 + 65)
            else:
                result += chr((ord(letter) - 97 + 13) % 26 + 97)
        else:
            result += letter
    return result
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           