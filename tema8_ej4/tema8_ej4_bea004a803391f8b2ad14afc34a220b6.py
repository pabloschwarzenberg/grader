def rot13(palabra):
    nuevaPalabra = ''
    for letter in palabra:
        n = ord(letter)+13
        if n >= 97+26:
            n -= 26
        nuevaPalabra += chr(n)
    return nuevaPalabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           