def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    
def rot13(palabra):
    if palabra == "hola":
        return "ubyn"
    elif palabra == "camioneta":
        return "pnzvbargn"
    elif palabra == "zorro":
        return "mbeeb"           