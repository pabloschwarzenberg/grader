def rot13(palabra):
    palabra=palabra.lower()
    palabra_lista=list(palabra)
    encriptada=[]
    for c in palabra_lista:
        if 97<=ord(c)<=109:
            c=chr(ord(c)+13)
            encriptada.append(c)
        elif 110<=ord(c)<=122:
            c=chr(ord(c)-13)
            encriptada.append(c)
    return ''.join(encriptada)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           