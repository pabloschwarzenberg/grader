def rot13(palabra):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = 'nopqrstuvwxyzabcdefghijklm'
    palabra_cifrada = ''
    posicion = 0

    for letra in palabra:
        if letra in abecedario:
            posicion = abecedario.index(letra)
            palabra_cifrada += cifrado[posicion]

    return palabra_cifrada
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           