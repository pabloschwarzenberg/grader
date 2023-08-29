def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = ''
    for i in message:
        if i in alphabet:
            if alphabet.index(i) < 13:
                string += alphabet[alphabet.index(i)+13]
            else:
                string += alphabet[alphabet.index(i)-13]
        elif i in alphabet.upper():
            if alphabet.upper().index(i) < 13:
                string += alphabet.upper()[alphabet.upper().index(i)+13]
            else:
                string += alphabet.upper()[alphabet.upper().index(i)-13]
        else:
            string += i
    return string
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
             
