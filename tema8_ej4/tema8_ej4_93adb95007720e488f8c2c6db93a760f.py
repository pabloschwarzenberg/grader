def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    traduc = ""
    for letra in palabra:
        traduc = traduc + abecedario[abecedario.find(letra) + 13]
        traduc = traduc.lower()
    return traduc


if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
