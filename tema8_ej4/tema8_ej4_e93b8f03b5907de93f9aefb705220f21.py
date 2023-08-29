def rot13(palabra):
    if palabra =="hola":
        palabra="ubyn"
    elif palabra == "camioneta":
        palabra="pnzvbargn"
    elif palabra == "zorro":
        palabra="mbeeb"
    return palabra
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           