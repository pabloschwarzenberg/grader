def rot13(palabra):
    traduccion = ""
    for i in palabra:
        if 65 <= ord(i) <= 90:
            if ord(i) <= 77:
                a = chr(ord(i)+13)
                traduccion += a
            elif 78 <= ord <= 90:
                a = chr(ord(i)-13)
                traduccion += a
        elif 97 <= ord(i) <= 122:
            if ord(i) <= 109:
                a = chr(ord(i)+13)
                traduccion += a
            elif 122 >= ord(i) >109:
                a = chr(ord(i)-13)
                traduccion += a
        else:
            a += i
    return traduccion

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           