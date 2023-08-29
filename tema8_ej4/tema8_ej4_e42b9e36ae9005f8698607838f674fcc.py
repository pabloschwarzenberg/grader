def rot13(palabra):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    traducido = ''
    for letra in palabra:
        i = abecedario.find(letra)
        if i != -1:
            if i > 12:
                traducido += abecedario[i - 13]
            else:
                traducido += abecedario[i + 13]
        else:
            traducido += letra
    return traducido

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           