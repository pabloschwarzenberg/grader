def rot13(palabra):
    resultado = ""
    for letra in palabra:
        f = ord(letra)
        if f >= ord('a') and f <= ord('z'):
            if f > ord('m'):
                f -= 13
            else:
                f += 13
        elif f >= ord('A') and f <= ord('Z'):
            if f > ord('M'):
                f -= 13
            else:
                f += 13
        resultado += chr(f)
    return resultado
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)           