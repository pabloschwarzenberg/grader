def rot13(palabra):
    palabra = list(palabra)
    i = 0
    while i < len(palabra):
        palabra[i] = (ord(palabra[i]) - 84) % 26
        i += 1
    newPalabra = []
    for l in palabra:
        newPalabra.append(chr(l + 97))
    newPalabra = "".join(newPalabra)
    return newPalabra
        
if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ").lower()
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)           