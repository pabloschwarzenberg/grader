h=[]
def rot13(palabra):
    resultado = ""

    for v in palabra:
        c = ord(v)

        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        resultado += chr(c)

    return resultado

    return h
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra=palabra.lower()
    print(palabra)
    palabra=list(palabra)
    resultado=rot13(palabra)
    resultado="".join(resultado)
    print("El resultado es: ",resultado)
           
   