def rot13(palabra):
    rot13 = []
    for e in palabra:
        if 97 <= ord(e) <= 109:
            print(ord(e))
            rot13.append(chr(ord(e)+13))
        elif 110 <= ord(e) <= 122:
            rot13.append(chr(ord(e)-13))
    return ''.join(rot13)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           