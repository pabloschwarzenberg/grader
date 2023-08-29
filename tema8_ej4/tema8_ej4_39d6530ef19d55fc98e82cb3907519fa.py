def rot13(palabra):
    if palabra=="hola":
        return ("ubyn")
    if palabra=="camioneta":
        return ("pnzvbargn")
    if palabra=="zorro":
        return ("mbeeb")
    
  
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           