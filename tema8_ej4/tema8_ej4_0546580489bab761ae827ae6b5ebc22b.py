def rot13(palabra):
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    encriptado = list("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    new_palabra = []
    for letra in palabra:
        new_palabra.append(encriptado[abecedario.index(letra)])
    palabra = ''.join(new_palabra)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           