def rot13(palabra):
    nueva=""
    for a in palabra:
        if ord(a)+13>122:
            b=ord(a)+13-122
            c=chr(96+b)
            nueva+=c
        else: 
            b=ord(a)+13
            c=chr(b)
            nueva+=c
        
    return nueva



if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           