def rot13(palabra):
    normal = "abcdefghijklmnopqrstuvwxyz"
    encrip = "nopqrstuvwxyzabcdefghijklm"
    encriptar = str.maketrans(normal,encrip)
    return palabra.translate(encriptar)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           