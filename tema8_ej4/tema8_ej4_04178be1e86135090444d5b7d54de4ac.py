def rot13(palabra):
    palabra2 = ""
    for letra in palabra:
        valor = ord(letra) #entrega el valor ascii de la letra
        if valor < 110:
            valor += 13
        else:
            valor -= 13
        palabra2 += chr(valor)
    return palabra2

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           