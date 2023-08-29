def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in message:
        if i in alphabet:
            if alphabet.index(i) < 13:
                string += alphabet[alphabet.index(i) + 13]
            else: string += alphabet[alphabet.index(i) -13]
        elif i in alphabet.upper():
            if alphabet.upper().index(i) < 13:
                string += alphabet.upper()[alphabet.upper().index(i) + 13]
            else: string += alphabet.upper()[alphabet.upper().index(i) -13]
        else: string += i
    return string
if __name__=="__main__":
    message=input("Ingresa la palabra que quieras encriptar: ")
    print("El resultado es: ",string)
           